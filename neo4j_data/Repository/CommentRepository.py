from neo4j_data.database_connect import Neo4jDriverSingleton


class CommentRepository:
    def __init__(self, driver):
        self.driver = driver

    def get_comments_by_post(self, post_id, sort_by="timestamp_desc"):
        """
        Fetch comments for a specific post with optional sorting.
        :param post_id: ID of the post
        :param sort_by: Sorting option ("timestamp_desc", "timestamp_asc", "upvotes_desc")
        :return: List of comments as dictionaries
        """
        with self.driver.session() as session:
            # Base query
            query = """
            // Find comments that reply directly to the post
            MATCH (p:Post {id: $post_id})<-[:REPLY_TO]-(c:Comment)
            OPTIONAL MATCH (c)-[:REPLY_TO]->(reply_to:Comment)
            OPTIONAL MATCH (u:User)-[:CREATED]->(c)
            RETURN c.id AS id, c.text AS text, c.timestamp AS timestamp,
                   coalesce(u.name, 'Unknown') AS author_name, 
                   coalesce(u.id, '') AS author_id,
                   reply_to.id AS reply_to_id, 
                   coalesce(c.reputation, 0) AS upvotes

            UNION

            // Find comments that reply to other comments
            MATCH (p:Post {id: $post_id})<-[:HAS_COMMENT]-(parent:Comment)<-[:REPLY_TO*0..]-(c:Comment)
            OPTIONAL MATCH (c)-[:REPLY_TO]->(reply_to:Comment)
            OPTIONAL MATCH (u:User)-[:CREATED]->(c)
            RETURN c.id AS id, c.text AS text, c.timestamp AS timestamp,
                   coalesce(u.name, 'Unknown') AS author_name, 
                   coalesce(u.id, '') AS author_id,
                   reply_to.id AS reply_to_id, 
                   coalesce(c.reputation, 0) AS upvotes
            """

            # Add sorting based on parameter
            if sort_by == "timestamp_desc":
                query += "\nORDER BY c.timestamp DESC"
            elif sort_by == "timestamp_asc":
                query += "\nORDER BY c.timestamp ASC"
            elif sort_by == "upvotes_desc":
                query += "\nORDER BY c.reputation DESC"

            result = session.run(query, post_id=post_id)
            return [dict(record) for record in result]

    def create_comment(self, post_id, user_id, text, reply_to_id=None):
        """
        Create a new comment on a post or as a reply to another comment.
        :param post_id: ID of the post.
        :param user_id: ID of the user creating the comment.
        :param text: Text content of the comment.
        :param reply_to_id: ID of the comment being replied to (optional).
        :return: The created comment as a dictionary.
        """
        with self.driver.session() as session:
            query = """
            MATCH (p:Post {id: $post_id})
            MATCH (u:User {id: $user_id})
            CREATE (c:Comment {id: apoc.create.uuid(), text: $text, timestamp: datetime(), reputation: 0})
            CREATE (u)-[:CREATED]->(c)
            CREATE (c)-[:REPLY_TO]->(p)
            WITH c, u
            OPTIONAL MATCH (reply_to:Comment {id: $reply_to_id})
            FOREACH (ignore IN CASE WHEN reply_to IS NOT NULL THEN [1] ELSE [] END |
                CREATE (c)-[:REPLY_TO]->(reply_to)
            )
            RETURN c.id AS id, c.text AS text, c.timestamp AS timestamp,
                   u.name AS author_name, u.id AS author_id,
                   reply_to.id AS reply_to_id, c.reputation AS upvotes
            """
            result = session.run(query, post_id=post_id, user_id=user_id, text=text, reply_to_id=reply_to_id)
            record = result.single()
            if record:
                comment = {
                    "id": record["id"],
                    "text": record["text"],
                    "timestamp": record["timestamp"],
                    "author_name": record["author_name"],
                    "author_id": record["author_id"],
                    "reply_to_id": record["reply_to_id"],
                    "upvotes": record["upvotes"] if record["upvotes"] is not None else 0,  # Default to 0 if reputation is missing
                }
                return comment
            else:
                raise ValueError("Failed to create comment.")

    def delete_comment(self, comment_id):
        """
        Delete a comment by its ID.
        :param comment_id: ID of the comment to delete.
        """
        with self.driver.session() as session:
            query = """
            MATCH (c:Comment {id: $comment_id})
            DETACH DELETE c
            """
            session.run(query, comment_id=comment_id)

    def upvote_comment(self, comment_id):
        """
        Increment the reputation (upvotes) of a comment.
        :param comment_id: ID of the comment to upvote.
        """
        with self.driver.session() as session:
            query = """
            MATCH (c:Comment {id: $comment_id})
            SET c.reputation = c.reputation + 1
            RETURN c.reputation AS upvotes
            """
            result = session.run(query, comment_id=comment_id)
            record = result.single()
            if record:
                return record["upvotes"]
            else:
                raise ValueError("Comment not found.")

    def downvote_comment(self, comment_id):
        """
        Decrement the reputation (upvotes) of a comment.
        :param comment_id: ID of the comment to downvote.
        """
        with self.driver.session() as session:
            query = """
            MATCH (c:Comment {id: $comment_id})
            SET c.reputation = c.reputation - 1
            RETURN c.reputation AS upvotes
            """
            result = session.run(query, comment_id=comment_id)
            record = result.single()
            if record:
                return record["upvotes"]
            else:
                raise ValueError("Comment not found.")