from neo4j_data.database_connect import Neo4jDriverSingleton
from datetime import datetime


class FriendRepository:
    def __init__(self, driver):
        self.driver = driver

    def send_friend_request(self, from_user_id, to_user_id):
        """
        Send a friend request from one user to another.
        """
        with self.driver.session() as session:
            query = """
            MATCH (from:User {id: $from_user_id}), (to:User {id: $to_user_id})
            MERGE (from)-[r:FRIEND_REQUEST {
                timestamp: datetime(),
                status: 'Pending'
            }]->(to)
            RETURN r.status AS status
            """
            result = session.run(query, from_user_id=from_user_id, to_user_id=to_user_id)
            return result.single()["status"]

    def accept_friend_request(self, from_user_id, to_user_id):
        """
        Accept a friend request and create a mutual friendship.
        """
        with self.driver.session() as session:
            query = """
            MATCH (from:User {id: $from_user_id})-[r:FRIEND_REQUEST]->(to:User {id: $to_user_id})
            WHERE r.status = 'Pending'
            DELETE r
            MERGE (from)-[:FRIEND_WITH {since: datetime()}]->(to)
            MERGE (to)-[:FRIEND_WITH {since: datetime()}]->(from)
            RETURN true AS success
            """
            result = session.run(query, from_user_id=from_user_id, to_user_id=to_user_id)
            return result.single()["success"]

    def reject_friend_request(self, from_user_id, to_user_id):
        """
        Reject a friend request.
        """
        with self.driver.session() as session:
            query = """
            MATCH (from:User {id: $from_user_id})-[r:FRIEND_REQUEST]->(to:User {id: $to_user_id})
            DELETE r
            RETURN true AS success
            """
            result = session.run(query, from_user_id=from_user_id, to_user_id=to_user_id)
            return result.single()["success"]

    def remove_friend(self, user1_id, user2_id):
        """
        Remove a friendship between two users.
        """
        with self.driver.session() as session:
            query = """
            MATCH (u1:User {id: $user1_id})-[r:FRIEND_WITH]-(u2:User {id: $user2_id})
            DELETE r
            RETURN count(r) AS relationships_deleted
            """
            result = session.run(query, user1_id=user1_id, user2_id=user2_id)
            return result.single()["relationships_deleted"] > 0

    def get_friends(self, user_id, limit=100, offset=0):
        """
        Get a user's friends with pagination.
        """
        with self.driver.session() as session:
            query = """
            MATCH (u:User {id: $user_id})-[:FRIEND_WITH]->(friend:User)
            RETURN friend.id AS id, 
                   friend.username AS username,
                   friend.email AS email,
                   friend.reputation AS reputation
            ORDER BY friend.username
            SKIP $offset LIMIT $limit
            """
            result = session.run(query, user_id=user_id, limit=limit, offset=offset)
            return [dict(record) for record in result]

    def get_pending_requests(self, user_id):
        """
        Get pending friend requests for a user (both sent and received).
        """
        with self.driver.session() as session:
            # Received requests
            query_received = """
            MATCH (from:User)-[r:FRIEND_REQUEST]->(to:User {id: $user_id})
            WHERE r.status = 'Pending'
            RETURN from.id AS from_id, 
                   from.username AS from_username,
                   r.timestamp AS timestamp,
                   'received' AS type
            """
            # Sent requests
            query_sent = """
            MATCH (from:User {id: $user_id})-[r:FRIEND_REQUEST]->(to:User)
            WHERE r.status = 'Pending'
            RETURN to.id AS to_id, 
                   to.username AS to_username,
                   r.timestamp AS timestamp,
                   'sent' AS type
            """

            received = session.run(query_received, user_id=user_id)
            sent = session.run(query_sent, user_id=user_id)

            return [
                *[dict(record) for record in received],
                *[dict(record) for record in sent]
            ]

    def are_friends(self, user1_id, user2_id):
        """
        Check if two users are friends.
        """
        with self.driver.session() as session:
            query = """
            MATCH (u1:User {id: $user1_id})-[:FRIEND_WITH]->(u2:User {id: $user2_id})
            RETURN count(*) > 0 AS are_friends
            """
            result = session.run(query, user1_id=user1_id, user2_id=user2_id)
            return result.single()["are_friends"]

    def get_friend_status(self, user1_id, user2_id):
        """
        Get the friendship status between two users.
        Returns: 'friends', 'pending_sent', 'pending_received', or 'none'
        """
        with self.driver.session() as session:
            # Check if already friends
            query_friends = """
            MATCH (u1:User {id: $user1_id})-[:FRIEND_WITH]->(u2:User {id: $user2_id})
            RETURN true AS is_friend
            """
            friends_result = session.run(query_friends, user1_id=user1_id, user2_id=user2_id)
            if friends_result.single() and friends_result.single()["is_friend"]:
                return "friends"

            # Check for pending requests
            query_requests = """
            MATCH (u1:User {id: $user1_id})-[r:FRIEND_REQUEST]->(u2:User {id: $user2_id})
            WHERE r.status = 'Pending'
            RETURN 'pending_sent' AS status
            UNION
            MATCH (u1:User {id: $user1_id})<-[r:FRIEND_REQUEST]-(u2:User {id: $user2_id})
            WHERE r.status = 'Pending'
            RETURN 'pending_received' AS status
            """
            requests_result = session.run(query_requests, user1_id=user1_id, user2_id=user2_id)
            record = requests_result.single()
            if record:
                return record["status"]

            return "none"