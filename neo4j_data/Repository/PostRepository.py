from neo4j_data.database_connect import Neo4jDriverSingleton

class PostRepository:
    def __init__(self, driver):
        self.driver = driver

    def get_all_posts(self, limit=10, offset=0):
        """
        Fetch posts with pagination.
        :param limit: Number of posts to fetch.
        :param offset: The offset for pagination.
        :return: List of posts as a dictionary.
        """
        with self.driver.session() as session:
            query = """
            MATCH (p:Post)<-[:CREATED]-(u:User)
            RETURN p.id AS id, p.title AS title, p.content AS content, p.timestamp AS timestamp, p.visibility AS visibility,
                   u.name AS author_name, u.id AS author_id
            ORDER BY p.timestamp DESC
            SKIP $offset LIMIT $limit
            """
            result = session.run(query, offset=offset, limit=limit)
            posts = [{
                "id": record["id"],
                "title": record["title"],
                "content": record["content"],
                "timestamp": record["timestamp"],
                "visibility": record["visibility"],
                "author_name": record["author_name"],
                "author_id": record["author_id"],
            } for record in result]
            return posts

    def get_posts_by_user(self, user_id):
        """
        Fetch posts created by a specific user.
        :param user_id: ID of the user.
        :return: List of posts, each post as a dictionary.
        """
        with self.driver.session() as session:
            query = """
            MATCH (p:Post)<-[:CREATED]-(u:User {id: $user_id})
            RETURN p.id AS id, p.title AS title, p.content AS content, p.timestamp AS timestamp, p.visibility AS visibility,
                   u.name AS author_name, u.id AS author_id
            ORDER BY p.timestamp DESC
            """
            result = session.run(query, user_id=user_id)
            posts = [{
                "id": record["id"],
                "title": record["title"],  # Added title
                "content": record["content"],
                "timestamp": record["timestamp"],
                "visibility": record["visibility"],
                "author_name": record["author_name"],
                "author_id": record["author_id"],
            } for record in result]
            return posts

    def create_post(self, user_id, title, content, visibility="PUBLIC"):
        """
        Create a new post with rich text content (HTML formatted).
        :param user_id: ID of the user creating the post.
        :param title: Title of the post.
        :param content: Content of the post (HTML formatted).
        :param visibility: Visibility of the post (default is 'PUBLIC').
        :return: The created post as a dictionary.
        """
        with self.driver.session() as session:
            query = """
            CREATE (p:Post {id: apoc.create.uuid(), title: $title, content: $content, timestamp: timestamp(), visibility: $visibility})
            WITH p
            MATCH (u:User {id: $user_id})
            CREATE (u)-[:CREATED]->(p)
            RETURN p.id AS id, p.title AS title, p.content AS content, p.timestamp AS timestamp, p.visibility AS visibility,
                   u.name AS author_name, u.id AS author_id
            """
            result = session.run(query, user_id=user_id, title=title, content=content, visibility=visibility)
            record = result.single()
            post = {
                "id": record["id"],
                "title": record["title"],
                "content": record["content"],  # HTML content is returned
                "timestamp": record["timestamp"],
                "visibility": record["visibility"],
                "author_name": record["author_name"],
                "author_id": record["author_id"],
            }
            return post


if __name__ == "__main__":
    driver = Neo4jDriverSingleton.get_instance()
    post_repo = PostRepository(driver)
    posts = post_repo.get_all_posts()
    for post in posts:
        print(post)
