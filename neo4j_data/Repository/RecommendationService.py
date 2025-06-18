import logging


class RecommendationService:
    def __init__(self, driver):
        self.driver = driver

    def get_recommended_posts(self, user_id, limit=10):
        logging.critical("RUN Recommendation settings")
        with self.driver.session() as session:
            query = """
                MATCH (u:User {id: $user_id})-[i:INTERACTED_WITH]->(p:Post)
                WITH u, COLLECT(p) AS seen_posts
                MATCH (rec:Post)
                WHERE NOT rec IN seen_posts
                OPTIONAL MATCH (u)-[int:INTERACTED_WITH]->(:Post)-[:TAGGED_AS]->(t)<-[:TAGGED_AS]-(rec)
                WITH rec, SUM(int.score) AS score
                RETURN rec ORDER BY score DESC, rec.timestamp DESC
                LIMIT $limit
            """
            result = session.run(query, user_id=user_id, limit=limit)
            return [record["rec"] for record in result]
