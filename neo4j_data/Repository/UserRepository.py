import uuid

class UserRepository:
    def __init__(self, driver):
        self.driver = driver

    def create(self, email, password):
        print(f"Debug: Creating user with password {password}")
        return create_user(self.driver, email, password)

    def read(self, email):
        user = read_user(self.driver, email)
        if user:
            print(f"Debug: Retrieved user with password {user['password']}")
        return user

    def update(self, user_id, name=None, age=None, email=None, password=None, reputation=None):
        return update_user(self.driver, user_id, name, age, email, password, reputation)

    def delete(self, user_id):
        return delete_user(self.driver, user_id)

    def check_password(self, stored_password, input_password):
        print(f"Debug: Checking password against stored password.")
        return stored_password == input_password  # Direct string comparison


def create_user(driver, email, password):
    """
    Create a new user node in the Neo4j database if the email doesn't already exist.
    """
    with driver.session() as session:
        with session.begin_transaction() as tx:
            # Check if a user with the same email already exists
            existing_user_query = """
            MATCH (u:User {email: $email})
            RETURN u
            """
            existing_user = tx.run(existing_user_query, email=email).single()

            if existing_user:
                return None  # User already exists

            user_id = str(uuid.uuid4())  # Generate a unique ID
            create_query = """
            CREATE (u:User {id: $id, email: $email, password: $password})
            RETURN u
            """
            result = tx.run(create_query, id=user_id, email=email, password=password)
            return result.single()[0]


def read_user(driver, email):
    """
    Retrieve a user node based on the email.
    """
    with driver.session() as session:
        with session.begin_transaction() as tx:
            read_query = """
            MATCH (u:User {email: $email})
            RETURN u.id AS id, u.email AS email, u.password AS password
            """
            result = tx.run(read_query, email=email)
            user = result.single()

            if user:
                return {
                    "id": user["id"],
                    "email": user["email"],
                    "password": user["password"],
                }
            return None


def update_user(driver, user_id, name=None, age=None, email=None, password=None, reputation=None):
    """
    Update a user's information.
    """
    with driver.session() as session:
        with session.begin_transaction() as tx:
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
            result = tx.run(update_query, user_id=user_id, name=name, age=age, email=email, password=password, reputation=reputation)
            return result.single()[0]


def delete_user(driver, user_id):
    """
    Delete a user node based on the user ID.
    """
    with driver.session() as session:
        with session.begin_transaction() as tx:
            delete_query = """
            MATCH (u:User {id: $user_id})
            DELETE u
            RETURN COUNT(u) AS deleted_count
            """
            result = tx.run(delete_query, user_id=user_id)
            deleted_count = result.single()["deleted_count"]
            return deleted_count > 0