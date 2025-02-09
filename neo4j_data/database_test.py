from neo4j import GraphDatabase


class Neo4jDriverSingleton:
    """
    Singleton class for interacting with Neo4j database
    """
    _instance = None

    def __new__(cls, uri, user, password):
        if cls._instance is None:
            cls._instance = super(Neo4jDriverSingleton, cls).__new__(cls)
            cls._instance._driver = GraphDatabase.driver(uri, auth=(user, password))
        return cls._instance

    def close(self):
        self._driver.close()

    def session(self):
        """
        Return a new session object for interacting with Neo4j.
        :return: Neo4j session
        """
        return self._driver.session()


# CRUD Functions for User

def create_user(session, user_id, name, age, email, reputation=0):
    """
    Create a new user node in the Neo4j database.
    :param session: Neo4j session
    :param user_id: Unique ID of the user
    :param name: Name of the user
    :param age: Age of the user
    :param email: Email of the user
    :param reputation: Reputation of the user
    :return: The created user node
    """
    create_query = """
    CREATE (u:User {id: $user_id, name: $name, age: $age, email: $email, reputation: $reputation})
    RETURN u
    """
    result = session.run(create_query, user_id=user_id, name=name, age=age, email=email, reputation=reputation)
    return result.single()[0]  # Return the created user node


def read_user(session, user_id):
    """
    Retrieve a user node based on the user ID.
    :param session: Neo4j session
    :param user_id: Unique ID of the user
    :return: The user node or None if not found
    """
    read_query = """
    MATCH (u:User {id: $user_id})
    RETURN u
    """
    result = session.run(read_query, user_id=user_id)
    user = result.single()
    if user:
        return user[0]  # Return the user node
    return None


def update_user(session, user_id, name=None, age=None, email=None, reputation=None):
    """
    Update a user's information.
    :param session: Neo4j session
    :param user_id: Unique ID of the user
    :param name: New name for the user (optional)
    :param age: New age for the user (optional)
    :param email: New email for the user (optional)
    :param reputation: New reputation for the user (optional)
    :return: The updated user node
    """
    update_query = """
    MATCH (u:User {id: $user_id})
    SET 
        u.name = COALESCE($name, u.name),
        u.age = COALESCE($age, u.age),
        u.email = COALESCE($email, u.email),
        u.reputation = COALESCE($reputation, u.reputation)
    RETURN u
    """
    result = session.run(update_query, user_id=user_id, name=name, age=age, email=email, reputation=reputation)
    return result.single()[0]  # Return the updated user node


def delete_user(session, user_id):
    """
    Delete a user node based on the user ID.
    :param session: Neo4j session
    :param user_id: Unique ID of the user
    :return: True if deletion was successful, False otherwise
    """
    delete_query = """
    MATCH (u:User {id: $user_id})
    DELETE u
    RETURN COUNT(u) AS deleted_count
    """
    result = session.run(delete_query, user_id=user_id)
    deleted_count = result.single()["deleted_count"]
    return deleted_count > 0  # Returns True if deletion was successful

# Main script to perform CRUD operations

if __name__ == "__main__":
    # Define Neo4j connection details
    neo4j_uri = "bolt://localhost:7687"
    neo4j_user = "neo4j"
    neo4j_password = "12345678"

    # Initialize the Neo4j driver
    neo4j_driver = Neo4jDriverSingleton(neo4j_uri, neo4j_user, neo4j_password)
    session = neo4j_driver.session()

    try:
        # 1. Create a user
        new_user = create_user(session, user_id="4", name="Daniel", age=29, email="daniel@example.com", reputation=10)
        print(f"Created User: {new_user['name']}")

        # 2. Read the user details
        user = read_user(session, user_id="4")
        if user:
            print(f"User Found: {user['name']}, {user['age']}, {user['email']}")
        else:
            print("User not found.")

        # 3. Update the user details
        updated_user = update_user(session, user_id="4", age=30, reputation=20)
        print(
            f"Updated User: {updated_user['name']}, Age: {updated_user['age']}, Reputation: {updated_user['reputation']}")

        # 4. Delete the user
        delete_success = delete_user(session, user_id="4")
        if delete_success:
            print("User deleted successfully.")
        else:
            print("Failed to delete the user.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        neo4j_driver.close()
