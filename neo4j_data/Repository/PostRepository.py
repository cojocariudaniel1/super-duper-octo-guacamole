from neo4j_data.database_connect import Neo4jDriverSingleton

class PostRepository:
    def __init__(self, driver):
        self.driver = driver

    def get_all_posts(self):
        """
        Fetch all posts from the database.
        :return: List of posts, each post as a dictionary.
        """
        with self.driver.session() as session:
            query = """
            MATCH (p:Post)<-[:CREATED]-(u:User)
            RETURN p.id AS id, p.content AS content, p.timestamp AS timestamp, p.visibility AS visibility,
                   u.name AS author_name, u.id AS author_id
            ORDER BY p.timestamp DESC
            """
            result = session.run(query)
            posts = [{
                "id": record["id"],
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
            RETURN p.id AS id, p.content AS content, p.timestamp AS timestamp, p.visibility AS visibility,
                   u.name AS author_name, u.id AS author_id
            ORDER BY p.timestamp DESC
            """
            result = session.run(query, user_id=user_id)
            posts = [{
                "id": record["id"],
                "content": record["content"],
                "timestamp": record["timestamp"],
                "visibility": record["visibility"],
                "author_name": record["author_name"],
                "author_id": record["author_id"],
            } for record in result]
            return posts
    def create_post(self, user_id):
        pass

if __name__ == "__main__":
    driver = Neo4jDriverSingleton.get_instance()
    a = PostRepository(driver)
    print(a.get_all_posts())