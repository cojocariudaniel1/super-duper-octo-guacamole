import time

from neo4j import GraphDatabase


class Neo4jDriverSingleton:
    _instance = None

    def __new__(cls, uri, user, password):
        if not cls._instance:
            cls._instance = GraphDatabase.driver(uri, auth=(user, password))
        return cls._instance


def read_nodes_in_batches(driver, batch_size=1000):
    query = """
    MATCH (n:Node)
    RETURN n.id AS id, n
    SKIP $skip
    LIMIT $limit
    """
    data = []
    with driver.session() as session:
        skip = 0
        while True:
            # Fetch nodes in batches
            result = session.run(query, skip=skip, limit=batch_size)
            nodes = list(result)

            if not nodes:  # Exit if no more nodes are returned
                break

            # Process the batch of nodes
            for record in nodes:
                data.append(record)
            skip += batch_size  # Move to the next batch of nodes

        print(data)
if __name__ == "__main__":
    # Initialize the Neo4j driver singleton
    driver = Neo4jDriverSingleton(uri="bolt://localhost:7687", user="neo4j", password="12345678")
    while True:
        read_nodes_in_batches(driver)
        time.sleep(980)
    # Run the node reading function in batches

