from neo4j import GraphDatabase

from neo4j_data.Repository.CommunityRepository import read_community, update_community, delete_community, \
    create_community
from neo4j_data.Repository.TagsRepository import create_tag, read_tag


def test_read_community():
    """
    Test the read_community function to retrieve a community by name.
    """
    uri = "bolt://localhost:7687"  # Adjust the URI if needed
    user = "neo4j"  # Your Neo4j username
    password = "12345678"  # Your Neo4j password

    driver = GraphDatabase.driver(uri, auth=(user, password))

    with driver.session() as session:
        # Test reading an existing community
        tag_name = "Tag_test2"  # Replace with the actual community name you want to test
        tag_create = create_tag(session, tag_name)
        tag_read = read_tag(session, tag_name)

        if tag_read:
            print(f"Tag found: {tag_name}")
        else:
            print("No community found.")


        # delete_comm = delete_community(session, community_name)
        driver.close()

if __name__ == "__main__":
    test_read_community()
