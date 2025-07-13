from datetime import datetime


class PostRepository:
    def __init__(self, driver):
        self.driver = driver

    def get_all_posts(self, limit=10, offset=0):
        with self.driver.session() as session:
            query = """
            MATCH (p:Post)<-[:CREATED]-(u:User)
            OPTIONAL MATCH (c:Community)-[:HAS_POST]->(p)
            RETURN p.id AS id, 
                   p.title AS title, 
                   p.content AS content, 
                   p.timestamp AS timestamp,
                   p.visibility AS visibility,
                   p.likes AS likes,
                   p.dislikes AS dislikes,
                   p.comments AS comments,
                   u.username AS author_name, 
                   u.id AS author_id,
                   u.img AS author_avatar,
                   c.name AS community_name,
                   c.icon AS community_icon
            ORDER BY p.timestamp DESC
            SKIP $offset LIMIT $limit   

            """
            result = session.run(query, offset=offset, limit=limit)
            posts = []
            for record in result:
                posts.append({
                    "id": record["id"],
                    "title": record["title"],
                    "content": record["content"],
                    "timestamp": self._format_timestamp(record["timestamp"]),
                    "visibility": record["visibility"],
                    "likes": record.get("likes", 0),
                    "dislikes": record.get("dislikes", 0),
                    "comments": record.get("comments", 0),
                    "author_name": record.get("author_name", "Unknown"),
                    "author_id": record.get("author_id", "Unknown"),
                    "author_avatar": record.get("author_avatar", "avatars/default_av.png"),
                    "community_name": record.get("community_name", ""),
                    "community_icon": record.get("community_icon", "communityIcons/communityIcon1.png")
                })
            return posts

    def get_post_by_post_id(self, post_id):
        """
        Fetch a single post by its unique ID.
        """
        with self.driver.session() as session:
            query = """
            MATCH (p:Post {id: $post_id})<-[:CREATED]-(u:User)
            OPTIONAL MATCH (p)-[:HAS_POST]->(c:Community)
            RETURN p.id AS id, 
                   p.title AS title, 
                   p.content AS content, 
                   p.timestamp AS timestamp,
                   p.visibility AS visibility,
                   p.likes AS likes,
                   p.dislikes AS dislikes,
                   p.comments AS comments,
                   u.username AS author_name, 
                   u.id AS author_id,
                   u.img AS author_avatar,
                   c.name AS community_name,
                   c.icon AS community_icon

            """
            result = session.run(query, post_id=post_id)
            record = result.single()

            if record:
                return {
                    "id": record["id"],
                    "title": record["title"],
                    "content": record["content"],
                    "timestamp": self._format_timestamp(record["timestamp"]),
                    "visibility": record["visibility"],
                    "likes": record.get("likes", 0),
                    "dislikes": record.get("dislikes", 0),
                    "comments": record.get("comments", 0),
                    "author_name": record["author_name"],
                    "author_id": record["author_id"],
                    "author_avatar": record.get("author_avatar", "avatars/default_av.png"),
                    "community_name": record.get("community_name", ""),
                    "community_icon": record.get("community_icon", "communityIcons/communityIcon1.png")
                }

            else:
                return None

    def get_posts_by_user(self, user_id):
        """
        Fetch posts created by a specific user.
        """
        with self.driver.session() as session:
            query = """
            MATCH (p:Post)<-[:CREATED]-(u:User {id: $user_id})
            OPTIONAL MATCH (p)-[:HAS_POST]->(c:Community)
            RETURN p.id AS id, 
                   p.title AS title, 
                   p.content AS content, 
                   p.timestamp AS timestamp,
                   p.visibility AS visibility,
                   p.likes AS likes,
                   p.dislikes AS dislikes,
                   p.comments AS comments,
                   u.username AS author_name, 
                   u.id AS author_id,
                   u.img AS author_avatar,
                   c.name AS community_name,
                   c.icon AS community_icon
            ORDER BY p.timestamp DESC
            """
            result = session.run(query, user_id=user_id)
            return [{
                "id": record["id"],
                "title": record["title"],
                "content": record["content"],
                "timestamp": self._format_timestamp(record["timestamp"]),
                "visibility": record["visibility"],
                "likes": record.get("likes", 0),
                "dislikes": record.get("dislikes", 0),
                "comments": record.get("comments", 0),
                "author_name": record["author_name"],
                "author_id": record["author_id"],
                "author_avatar": record.get("author_avatar", "avatars/default_av.png"),
                "community_name": record.get("community_name", ""),
                "community_icon": record.get("community_icon", "communityIcons/communityIcon1.png")
            } for record in result]

    def create_post(self, user_id, title, content, visibility="PUBLIC", community_name=None):
        """
        Create a new post with all required fields.
        """
        with self.driver.session() as session:
            query = """
            MATCH (u:User {id: $user_id})
            CREATE (p:Post {
                id: randomUUID(), 
                title: $title, 
                content: $content, 
                timestamp: datetime(), 
                visibility: $visibility,
                likes: 0,
                dislikes: 0,
                comments: 0
            })
            CREATE (u)-[:CREATED]->(p)
            """

            if community_name:
                query += """
                WITH p, u
                MATCH (c:Community {name: $community_name})
                CREATE (c)-[:HAS_POST]->(p)
                """

            query += """
            RETURN p.id AS id, 
                   p.title AS title, 
                   p.content AS content, 
                   p.timestamp AS timestamp, 
                   p.visibility AS visibility,
                   u.username AS author_name, 
                   u.id AS author_id
            """

            params = {
                "user_id": user_id,
                "title": title,
                "content": content,
                "visibility": visibility
            }

            if community_name:
                params["community_name"] = community_name

            result = session.run(query, params)
            record = result.single()

            return {
                "id": record["id"],
                "title": record["title"],
                "content": record["content"],
                "timestamp": self._format_timestamp(record["timestamp"]),
                "visibility": record["visibility"],
                "author_name": record["author_name"],
                "author_id": record["author_id"]
            }

    def _format_timestamp(self, timestamp):
        """
        Format timestamp to a human-readable relative time.
        Handles both Neo4j DateTime objects and string timestamps.
        """
        # Convert Neo4j DateTime to Python datetime if needed
        if hasattr(timestamp, 'to_native'):
            timestamp = timestamp.to_native()
        elif isinstance(timestamp, str):
            timestamp = datetime.fromisoformat(timestamp)

        # Make both datetimes offset-naive or offset-aware
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

    def increment_post_points(self, post_id, increment=1, is_like=True, user_id=None):
        """
        Increment or decrement a post's points and record the user interaction.
        """
        with self.driver.session() as session:
            field = "likes" if is_like else "dislikes"

            # Step 1: Update post's like/dislike count
            query = f"""
            MATCH (p:Post {{id: $post_id}})
            SET p.{field} = coalesce(p.{field}, 0) + $increment
            RETURN p.{field} AS points
            """
            result = session.run(query, post_id=post_id, increment=increment)
            record = result.single()
            points = record["points"]

            # Step 2: Update interaction score for recommendation
            if user_id:
                interaction_query = """
                MATCH (u:User {id: $user_id}), (p:Post {id: $post_id})
                MERGE (u)-[r:INTERACTED_WITH]->(p)
                ON CREATE SET r.score = $score
                ON MATCH SET r.score = r.score + $score
                """
                session.run(interaction_query, user_id=user_id, post_id=post_id, score=3)

            return points

    def add_comment_to_post(self, post_id, user_id, content):
        """
        Add a comment to a post.
        """
        with self.driver.session() as session:
            # First create the comment
            query = """
            MATCH (p:Post {id: $post_id})
            MATCH (u:User {id: $user_id})
            CREATE (c:Comment {
                id:  randomUUID(),
                content: $content,
                timestamp: datetime(),
                likes: 0,
                dislikes: 0
            })
            CREATE (u)-[:CREATED]->(c)
            CREATE (c)-[:COMMENT_ON]->(p)

            // Increment the post's comment count
            SET p.comments = coalesce(p.comments, 0) + 1

            RETURN c.id AS id, 
                   c.content AS content, 
                   c.timestamp AS timestamp,
                   u.username AS author_name,
                   u.id AS author_id,
                   u.img AS author_avatar

            """
            result = session.run(query, post_id=post_id, user_id=user_id, content=content)
            record = result.single()

            return {
                "id": record["id"],
                "content": record["content"],
                "timestamp": self._format_timestamp(record["timestamp"]),
                "author_name": record["author_name"],
                "author_id": record["author_id"],
                "author_avatar": record.get("author_avatar", "avatars/default_av.png")
            }
