from neo4j import GraphDatabase

class Neo4jDriverSingleton:
    """
    Singleton class for managing the Neo4j database connection.
    """
    _instance = None

    def __new__(cls, uri="bolt://localhost:7687", user="neo4j", password="12345678"):
        if cls._instance is None:
            cls._instance = super(Neo4jDriverSingleton, cls).__new__(cls)
            cls._instance._driver = GraphDatabase.driver(uri, auth=(user, password))
        return cls._instance

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = Neo4jDriverSingleton()
        return cls._instance

    def session(self):
        """ Returnează o sesiune activă. """
        return self._driver.session()

    def close(self):
        """ Închide conexiunea cu baza de date. """
        self._driver.close()
