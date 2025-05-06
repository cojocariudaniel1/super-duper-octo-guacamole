from neo4j_data.Repository.CommentRepository import CommentRepository
from neo4j_data.database_connect import Neo4jDriverSingleton

# Connect to Neo4j
driver = Neo4jDriverSingleton(uri="bolt://localhost:7687", user="neo4j", password="12345678").get_driver()
repo = CommentRepository(driver)

# Step 1: Setup test User and Post nodes
def setup_test_data():
    with driver.session() as session:
        session.run("""
        MERGE (u:User {id: 'user123'}) 
        SET u.username = 'test_user'
        """)
        session.run("""
        MERGE (p:Post {id: 'post123'}) 
        SET p.title = 'Test Post'
        """)
    print("✔ Test User and Post created.")

# Step 2: Test creating a comment
def test_create_comment():
    comment = repo.create_comment(post_id="post123", user_id="user123", text="This is a test comment.")
    print("📝 Created Comment:", comment)
    return comment["id"]

# Step 3 (Optional): Test replying to the above comment
def test_reply_to_comment(parent_comment_id):
    reply = repo.create_comment(
        post_id="post123",
        user_id="user123",
        text="This is a reply to the test comment.",
        reply_to_id=parent_comment_id
    )
    print("↩️ Created Reply:", reply)

# Run the test
if __name__ == "__main__":
    setup_test_data()
    comment_id = test_create_comment()
    test_reply_to_comment(comment_id)
