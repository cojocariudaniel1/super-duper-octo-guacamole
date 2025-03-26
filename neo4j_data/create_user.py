from neo4j import GraphDatabase


class Neo4jDriverSingleton:
    _instance = None

    def __new__(cls, uri, user, password):
        if not cls._instance:
            cls._instance = GraphDatabase.driver(uri, auth=(user, password))
        return cls._instance


def create_nodes_and_relationships(driver, user_id):
    query = """
    MERGE (u:User {id: $user_id})  // Ensure the user node exists
    WITH u
    UNWIND range(1, 10000) AS i  // Create 500k nodes
    CREATE (n:Node {id: i})
    MERGE (n)-[:RELATED_TO]->(u)  // Create relationships to the user
    """

    with driver.session() as session:
        session.run(query, user_id=user_id)


if __name__ == "__main__":
    # Initialize the Neo4j driver singleton
    driver = Neo4jDriverSingleton(uri="bolt://localhost:7687", user="neo4j", password="12345678")

    # Define the user ID you want to relate the nodes to
    user_id = "12345"
    for i in range(100):
        create_nodes_and_relationships(driver, user_id)

    # Run the node creation and relationship creation process
    print("500,000 nodes created and relationships established.")
