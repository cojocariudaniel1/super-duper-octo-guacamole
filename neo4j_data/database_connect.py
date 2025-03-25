from neo4j import GraphDatabase

class Neo4jDriverSingleton:
    _instance = None
    _driver = None

    def __new__(cls, uri=None, user=None, password=None):
        if cls._instance is None:
            cls._instance = super(Neo4jDriverSingleton, cls).__new__(cls)
            if uri and user and password:
                cls._driver = GraphDatabase.driver(uri, auth=(user, password))
        return cls._instance

    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            raise ValueError("Driver not initialized. Please create an instance with credentials first.")
        return cls._driver

    @classmethod
    def close_driver(cls):
        if cls._driver is not None:
            cls._driver.close()
            cls._driver = None
            cls._instance = None