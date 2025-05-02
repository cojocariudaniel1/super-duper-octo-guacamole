from neo4j_data.database_connect import Neo4jDriverSingleton
from datetime import datetime


class CommunityRepository:
    def __init__(self, driver):
        self.driver = driver

    def create_community(self, name, description, privacy_level="public", reputation_required=0, banner_image=None, icon=None):
        """
        Create a new community if it doesn't exist already.
        """
        with self.driver.session() as session:
            result = session.run("""
                MERGE (c:Community {name: $name})
                ON CREATE SET 
                    c.id = apoc.create.uuid(),
                    c.description = $description,
                    c.privacy_level = $privacy_level,
                    c.reputation_required = $reputation_required,
                    c.banner_image = $banner_image,
                    c.icon = $icon,
                    c.created_at = datetime()
                RETURN c
            """, {
                "name": name,
                "description": description,
                "privacy_level": privacy_level,
                "reputation_required": reputation_required,
                "banner_image": banner_image,
                "icon": icon
            })
            record = result.single()
            if record:
                return self._format_community(record["c"])
            return None

    def get_community(self, name):
        """
        Retrieve a community by name.
        """
        with self.driver.session() as session:
            result = session.run("""
                MATCH (c:Community {name: $name})
                RETURN c
            """, {"name": name})
            record = result.single()
            return self._format_community(record["c"]) if record else None

    def update_community(self, name, description=None, privacy_level=None, reputation_required=None, banner_image=None, icon=None):
        """
        Update an existing community.
        """
        updates = []
        if description is not None:
            updates.append("c.description = $description")
        if privacy_level is not None:
            updates.append("c.privacy_level = $privacy_level")
        if reputation_required is not None:
            updates.append("c.reputation_required = $reputation_required")
        if banner_image is not None:
            updates.append("c.banner_image = $banner_image")
        if icon is not None:
            updates.append("c.icon = $icon")

        if not updates:
            return None  # No fields to update

        set_clause = ", ".join(updates)

        with self.driver.session() as session:
            result = session.run(f"""
                MATCH (c:Community {{name: $name}})
                SET {set_clause}
                RETURN c
            """, {
                "name": name,
                "description": description,
                "privacy_level": privacy_level,
                "reputation_required": reputation_required,
                "banner_image": banner_image,
                "icon": icon
            })
            record = result.single()
            return self._format_community(record["c"]) if record else None

    def delete_community(self, name):
        """
        Delete a community by name.
        """
        with self.driver.session() as session:
            result = session.run("""
                MATCH (c:Community {name: $name})
                DETACH DELETE c
                RETURN COUNT(*) AS deleted_count
            """, {"name": name})
            record = result.single()
            return record["deleted_count"] > 0

    def get_all_communities(self, limit=10, offset=0):
        """
        Retrieve a list of communities with pagination.
        """
        with self.driver.session() as session:
            result = session.run("""
                MATCH (c:Community)
                RETURN c
                ORDER BY c.created_at DESC
                SKIP $offset LIMIT $limit
            """, {"offset": offset, "limit": limit})
            return [self._format_community(record["c"]) for record in result]

    def _format_community(self, node):
        """
        Format the community node data into a dictionary.
        """
        created_at = node.get("created_at")
        return {
            "id": node.get("id"),
            "name": node.get("name"),
            "description": node.get("description"),
            "privacy_level": node.get("privacy_level"),
            "reputation_required": node.get("reputation_required", 0),
            "banner_image": node.get("banner_image"),
            "icon": node.get("icon"),
            "created_at": self._format_timestamp(created_at) if created_at else None
        }

    def _format_timestamp(self, timestamp):
        """
        Format timestamp to a human-readable relative time.
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

    # In CommunityRepository class
    def get_top_communities(self, limit=4):
        """
        Retrieve top communities by member count with optional limit.
        """
        with self.driver.session() as session:
            result = session.run("""
                MATCH (c:Community)
                OPTIONAL MATCH (c)<-[:MEMBER_OF]-(u:User)
                WITH c, COUNT(u) AS member_count
                RETURN c
                ORDER BY member_count DESC
                LIMIT $limit
            """, {"limit": limit})
            return [self._format_community(record["c"]) for record in result]
