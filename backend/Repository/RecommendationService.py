import logging

from backend.database_connect import Neo4jDriverSingleton


class RecommendationService:
    def __init__(self, driver):
        self.driver = driver

    def get_recommended_posts(self, user_id, limit=10):
        with self.driver.session() as session:
            query = """
            MATCH (u:User {id: $user_id})-[i:INTERACTED_WITH]->(p:Post)
            WITH u, COLLECT(p.id) AS seen_post_ids 
            
            MATCH (rec:Post)<-[:CREATED]-(author:User)
            WHERE NOT rec.id IN seen_post_ids          
            
            OPTIONAL MATCH (c:Community)-[:HAS_POST]->(rec)
            OPTIONAL MATCH (u)-[int:INTERACTED_WITH]->(:Post)-[:TAGGED_AS]->(t)<-[:TAGGED_AS]-(rec)
            
            WITH rec, author, c,
                 COALESCE(SUM(int.score), 0) AS score,
                 rec.likes AS likes,
                 rec.dislikes AS dislikes,
                 rec.comments AS comments            
            
            RETURN rec.id AS id,
                   rec.title AS title,
                   rec.content AS content,
                   rec.timestamp AS timestamp,
                   COALESCE(likes, 0) AS likes,
                   COALESCE(dislikes, 0) AS dislikes,
                   COALESCE(comments, 0) AS comments,
                   score,
                   author.username AS author_name,
                   author.id AS author_id,
                   author.img AS author_avatar,
                   c.name AS community_name,
                   c.icon AS community_icon
            ORDER BY score DESC, timestamp DESC
            LIMIT $limit
            """
            result = session.run(query, user_id=user_id, limit=limit)
            results = []
            for record in result:
                results.append({
                    "id": record["id"],
                    "title": record["title"],
                    "content": record["content"],
                    "timestamp": record["timestamp"],
                    "likes": record["likes"],
                    "dislikes": record["dislikes"],
                    "comments": record["comments"],
                    "author_name": record["author_name"],
                    "author_id": record["author_id"],
                    "author_avatar": record.get("author_avatar", "avatars/default_av.png"),
                    "community_name": record.get("community_name", ""),
                    "community_icon": record.get("community_icon", "communityIcons/communityIcon1.png"),
                    "score": record["score"]
                })
            logging.critical(f"RECOMMENDED POSTS: {results}")
            return results

if __name__ == "__main__":
    Neo4jDriverSingleton(uri="bolt://localhost:7687", user="neo4j", password="12345678")
    posts_repo = RecommendationService(Neo4jDriverSingleton.get_driver())
    posts = posts_repo.get_recommended_posts("38599")
    print(posts)