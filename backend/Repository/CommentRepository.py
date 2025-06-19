import logging

from backend.database_connect import Neo4jDriverSingleton
from datetime import datetime


class CommentRepository:
    def __init__(self, driver):
        self.driver = driver

    def get_comments_for_post(self, post_id):
        """
        Fetch all comments for a post with their hierarchy and author information
        """
        with self.driver.session() as session:
            query = """
            MATCH (p:Post {id: $post_id})
            OPTIONAL MATCH (p)-[:HAS_COMMENT]->(c:Comment)
            OPTIONAL MATCH (c)-[:REPLY_TO]->(parent:Comment)
            OPTIONAL MATCH (u:User)-[:CREATED]->(c)
            RETURN c.id AS id,
                   c.text AS text,
                   c.timestamp AS timestamp,
                   c.likes AS likes,
                   c.dislikes AS dislikes,
                   u.username AS author_name,
                   u.id AS author_id,
                   parent.id AS parent_id
            ORDER BY c.timestamp ASC
            """
            result = session.run(query, post_id=post_id)

            comments = []
            for record in result:
                print(record)
                if record["id"] is None:  # Skip if no comments found
                    continue

                comments.append({
                    "id": record["id"],
                    "text": record["text"],
                    "timestamp": self._format_timestamp(record["timestamp"]),
                    "likes": record.get("likes", 0),
                    "dislikes": record.get("dislikes", 0),
                    "author_name": record["author_name"],
                    "author_id": record["author_id"],
                    "parent_id": record.get("parent_id")
                })
            return self._build_comment_tree(comments)

    def add_comment_to_post(self, post_id, user_id, text, parent_comment_id=None):
        """
        Add a comment to a post or as a reply to another comment
        """
        with self.driver.session() as session:
            comment_id = str(datetime.now().timestamp())  # Simple unique ID for demo

            if parent_comment_id:
                # For replies to existing comments
                query = """
                MATCH (u:User {id: $user_id})
                MATCH (parent:Comment {id: $parent_comment_id})
                MATCH (p:Post {id: $post_id})
                CREATE (c:Comment {
                    id: $comment_id,
                    text: $text,
                    timestamp: datetime(),
                    likes: 0,
                    dislikes: 0
                })
                CREATE (u)-[:CREATED]->(c)
                CREATE (c)-[:REPLY_TO]->(parent)
                CREATE (c)-[:COMMENT_ON]->(p)
                RETURN c.id AS id,
                       c.text AS text,
                       c.timestamp AS timestamp,
                       u.username AS author_name,
                       u.id AS author_id,
                       parent.id AS parent_id
                """
                params = {
                    "post_id": post_id,
                    "user_id": user_id,
                    "text": text,
                    "parent_comment_id": parent_comment_id,
                    "comment_id": comment_id
                }
            else:
                # For top-level comments on posts
                query = """
                MATCH (u:User {id: $user_id})
                MATCH (p:Post {id: $post_id})
                CREATE (c:Comment {
                    id: $comment_id,
                    text: $text,
                    timestamp: datetime(),
                    likes: 0,
                    dislikes: 0
                })
                CREATE (u)-[:CREATED]->(c)
                CREATE (c)-[:COMMENT_ON]->(p)

                // Update post comment count
                SET p.comments = coalesce(p.comments, 0) + 1

                RETURN c.id AS id,
                       c.text AS text,
                       c.timestamp AS timestamp,
                       u.username AS author_name,
                       u.id AS author_id,
                       null AS parent_id
                """
                params = {
                    "post_id": post_id,
                    "user_id": user_id,
                    "text": text,
                    "comment_id": comment_id
                }

            result = session.run(query, params)
            record = result.single()
            if record:
                return {
                    "id": record["id"],
                    "text": record["text"],
                    "timestamp": self._format_timestamp(record["timestamp"]),
                    "author_name": record["author_name"],
                    "author_id": record["author_id"],
                    "parent_id": record.get("parent_id")
                }
            else:
                logging.critical("Records is null")

    def increment_comment_points(self, comment_id, increment=1, is_like=True):
        """
        Increment or decrement a comment's points
        """
        with self.driver.session() as session:
            field = "likes" if is_like else "dislikes"
            query = f"""
            MATCH (c:Comment {{id: $comment_id}})
            SET c.{field} = coalesce(c.{field}, 0) + $increment
            RETURN c.{field} AS points
            """
            result = session.run(query, comment_id=comment_id, increment=increment)
            record = result.single()
            return record["points"]

    def _build_comment_tree(self, comments):
        """
        Convert flat list of comments into hierarchical tree structure
        """
        comment_map = {}
        root_comments = []

        # First pass: create map of all comments
        for comment in comments:
            comment["replies"] = []
            comment_map[comment["id"]] = comment

        # Second pass: build hierarchy
        for comment in comments:
            if comment["parent_id"]:
                parent = comment_map.get(comment["parent_id"])
                if parent:
                    parent["replies"].append(comment)
            else:
                root_comments.append(comment)

        return root_comments

    def _format_timestamp(self, timestamp):
        """
        Format timestamp to relative time string
        """
        if hasattr(timestamp, 'to_native'):
            timestamp = timestamp.to_native()
        elif isinstance(timestamp, str):
            timestamp = datetime.fromisoformat(timestamp)

        now = datetime.now(timestamp.tzinfo if timestamp.tzinfo else None)
        delta = now - timestamp

        if delta.days > 365:
            return f"{delta.days // 365} years ago"
        if delta.days > 30:
            return f"{delta.days // 30} months ago"
        if delta.days > 0:
            return f"{delta.days} days ago"
        if delta.seconds > 3600:
            return f"{delta.seconds // 3600} hours ago"
        if delta.seconds > 60:
            return f"{delta.seconds // 60} minutes ago"
        return "Just now"

if __name__ == "__main__":
    Neo4jDriverSingleton(uri="bolt://localhost:7687", user="neo4j", password="12345678")
    comment_repo = CommentRepository(Neo4jDriverSingleton.get_driver())
    comments = comment_repo.get_comments_for_post("101")
    print(comments)