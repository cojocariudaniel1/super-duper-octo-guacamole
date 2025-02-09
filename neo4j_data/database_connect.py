from neo4j import GraphDatabase

class Neo4jDriverSingleton:
    """
    Singleton class for managing the Neo4j database connection.
    """
    _instance = None

    def __new__(cls, uri, user, password):
        if cls._instance is None:
            cls._instance = super(Neo4jDriverSingleton, cls).__new__(cls)
            cls._instance._driver = GraphDatabase.driver(uri, auth=(user, password))
        return cls._instance

    def session(self):
        """
        Return a new session object for interacting with Neo4j.
        :return: Neo4j session
        """
        return self._driver.session()

    def close(self):
        """
        Close the Neo4j driver connection.
        """
        self._driver.close()
