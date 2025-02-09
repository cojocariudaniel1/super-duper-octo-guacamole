import uuid  # Add this import at the top of the file


class UserRepository:
    def __init__(self, session):
        self.session = session

    def create(self, email, password):
        print(f"Debug: Creating user with password {password}")
        return create_user(self.session, email, password)

    def read(self, email):
        user = read_user(self.session, email)
        if user:
            print(f"Debug: Retrieved user with password {user['password']}")
        return user

    def update(self, email, name=None, age=None, password=None, reputation=None):
        return update_user(self.session, email, name, age, password, reputation)

    def delete(self, email):
        return delete_user(self.session, email)

    def check_password(self, stored_password, input_password):
        print(f"Debug: Checking password '{input_password}' against stored password '{stored_password}'")
        return stored_password == input_password  # Compare as plain text


def create_user(session, email, password):
    """
    Create a new user node in the Neo4j database if the email doesn't already exist.
    :param session: Neo4j session
    :param email: Email of the user
    :param password: Plain text password of the user
    :return: The created user node or None if the user already exists
    """
    # Check if a user with the same email already exists
    existing_user_query = """
    MATCH (u:User {email: $email})
    RETURN u
    """
    existing_user = session.run(existing_user_query, email=email).single()

    if existing_user:
        return None  # User already exists
    else:
        create_query = """
        CREATE (u:User {email: $email, password: $password})
        RETURN u
        """
        result = session.run(create_query, email=email, password=password)
        return result.single()[0]


def read_user(session, email):
    """
    Retrieve a user node based on the email.
    :param session: Neo4j session
    :param email: Email of the user
    :return: The user node or None if not found
    """
    read_query = """
    MATCH (u:User {email: $email})
    RETURN u.id AS id, u.email AS email, u.password AS password
    """
    result = session.run(read_query, email=email)
    user = result.single()
    if user:
        return {
            "id": user["id"],
            "email": user["email"],
            "password": user["password"],  # Return the plain text password
        }
    return None


def update_user(session, user_id, name=None, age=None, email=None, password=None, reputation=None):
    """
    Update a user's information.
    :param session: Neo4j session
    :param user_id: Unique ID of the user
    :param name: New name for the user (optional)
    :param age: New age for the user (optional)
    :param email: New email for the user (optional)
    :param password: New password for the user (optional)
    :param reputation: New reputation for the user (optional)
    :return: The updated user node
    """
    update_query = """
    MATCH (u:User {id: $user_id})
    SET 
        u.name = COALESCE($name, u.name),
        u.age = COALESCE($age, u.age),
        u.email = COALESCE($email, u.email),
        u.password = COALESCE($password, u.password),
        u.reputation = COALESCE($reputation, u.reputation)
    RETURN u
    """
    result = session.run(update_query, user_id=user_id, name=name, age=age, email=email, password=password, reputation=reputation)
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
