from neo4j_data.database_connect import Neo4jDriverSingleton
from datetime import datetime


class SessionRepository:
    def __init__(self, driver):
        self.driver = driver

    def create_session(self, user_id, session_id=None):
        """
        Create a new session for a user.
        If session_id is not provided, a new one will be generated.
        """
        with self.driver.session() as session:
            query = """
            MATCH (u:User {id: $user_id})
            MERGE (u)-[:HAS_SESSION]->(s:Session {
                id: coalesce($session_id, randomUUID()),
                status: 'Active',
                last_active: datetime()
            })
            RETURN s.id AS session_id
            """
            result = session.run(query, user_id=user_id, session_id=session_id)
            return result.single()["session_id"]

    def update_session_activity(self, session_id):
        """
        Update the last_active timestamp of a session.
        """
        with self.driver.session() as session:
            query = """
            MATCH (s:Session {id: $session_id})
            SET s.last_active = datetime()
            RETURN s.id AS session_id
            """
            result = session.run(query, session_id=session_id)
            return result.single()["session_id"]

    def end_session(self, session_id):
        """
        End a session by setting its status to 'Inactive'.
        """
        with self.driver.session() as session:
            query = """
            MATCH (s:Session {id: $session_id})
            SET s.status = 'Inactive'
            RETURN s.id AS session_id
            """
            result = session.run(query, session_id=session_id)
            return result.single()["session_id"]

    def get_active_sessions(self, user_id):
        """
        Get all active sessions for a user.
        """
        with self.driver.session() as session:
            query = """
            MATCH (u:User {id: $user_id})-[:HAS_SESSION]->(s:Session)
            WHERE s.status = 'Active'
            RETURN s.id AS session_id, s.last_active AS last_active
            ORDER BY s.last_active DESC
            """
            result = session.run(query, user_id=user_id)
            return [{
                "session_id": record["session_id"],
                "last_active": record["last_active"].to_native()
            } for record in result]

    def validate_session(self, session_id, user_id=None):
        """
        Validate if a session exists and is active.
        Optionally verify it belongs to a specific user.
        """
        with self.driver.session() as session:
            query = """
            MATCH (s:Session {id: $session_id})
            WHERE s.status = 'Active'
            OPTIONAL MATCH (u:User)-[:HAS_SESSION]->(s)
            RETURN 
                CASE WHEN s IS NOT NULL THEN true ELSE false END AS is_valid,
                u.id AS user_id
            """
            result = session.run(query, session_id=session_id)
            record = result.single()

            is_valid = record["is_valid"]
            if user_id and is_valid:
                is_valid = record["user_id"] == user_id

            return is_valid

    def cleanup_inactive_sessions(self, days_inactive=30):
        """
        Clean up sessions that have been inactive for more than X days.
        Returns number of sessions deleted.
        """
        with self.driver.session() as session:
            query = """
            MATCH (s:Session)
            WHERE datetime() > s.last_active + duration({days: $days_inactive})
            AND s.status = 'Active'
            DETACH DELETE s
            RETURN count(s) AS sessions_deleted
            """
            result = session.run(query, days_inactive=days_inactive)
            return result.single()["sessions_deleted"]