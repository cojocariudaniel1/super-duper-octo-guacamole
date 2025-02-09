import unittest

from neo4j_data.Repository.UserRepository import UserRepository
from neo4j_data.database_connect import Neo4jDriverSingleton


class TestUserRepository(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up Neo4j connection and repository before tests."""
        cls.neo4j_driver = Neo4jDriverSingleton("bolt://localhost:7687", "neo4j", "12345678")
        cls.session = cls.neo4j_driver.session()
        cls.user_repo = UserRepository(cls.session)

    @classmethod
    def tearDownClass(cls):
        """Clean up by closing the Neo4j session and driver after tests."""
        cls.session.close()
        cls.neo4j_driver.close()

    def test_create_user(self):
        """Test creating a user."""
        # Ensure the user with ID '123' doesn't exist before the test
        self.user_repo.delete("123")  # Delete if the user already exists

        # Now create the user
        user = self.user_repo.create("123", "John Doe", 30, "johndoe@example.com", 10)
        self.assertIsNotNone(user, "User should be created successfully.")
        self.assertEqual(user["name"], "John Doe")
        self.assertEqual(user["age"], 30)
        self.assertEqual(user["email"], "johndoe@example.com")
        self.assertEqual(user["reputation"], 10)

    def test_read_user(self):
        """Test reading an existing user."""
        # First, create a user
        self.user_repo.create("124", "Jane Doe", 28, "janedoe@example.com", 15)

        # Read the user
        user = self.user_repo.read("124")
        self.assertIsNotNone(user, "User should be found.")
        self.assertEqual(user["name"], "Jane Doe")
        self.assertEqual(user["email"], "janedoe@example.com")

    def test_update_user(self):
        """Test updating an existing user."""
        # Create a user
        self.user_repo.create("125", "Alice", 25, "alice@example.com", 20)

        # Update the user
        updated_user = self.user_repo.update("125", age=26, reputation=25)
        self.assertIsNotNone(updated_user, "User should be updated successfully.")
        self.assertEqual(updated_user["age"], 26)
        self.assertEqual(updated_user["reputation"], 25)

    def test_delete_user(self):
        """Test deleting a user."""
        # Create a user
        self.user_repo.create("126", "Bob", 32, "bob@example.com", 30)

        # Delete the user
        delete_success = self.user_repo.delete("126")
        self.assertTrue(delete_success, "User should be deleted successfully.")

        # Try to read the deleted user (should return None)
        user = self.user_repo.read("126")
        self.assertIsNone(user, "User should not be found after deletion.")

if __name__ == "__main__":
    unittest.main()
