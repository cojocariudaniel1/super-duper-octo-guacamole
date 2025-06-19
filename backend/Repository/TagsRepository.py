import uuid  # Add this import at the top of the file


class TagsRepository:
    def __init__(self, session):
        self.session = session

    def create(self, name):
        return create_tag(self.session, name)

    def read(self, name):
        tag_name = read_tag(self.session, name)

        return tag_name

    def update(self, name=None):
        return update_tag(self.session, name)

    def delete(self, name):
        return delete_tag(self.session, name)

def create_tag(session, name):
    """
    Create a new user node in the Neo4j database if the email doesn't already exist.
    :param session: Neo4j session
    :param name: Plain text tag name
    :return: The created tag node or None if the tag already exists
    """
    # Check if the tag with the same name already exists
    existing_tag_query = """
    MATCH (u:Tag {name: $name})
    RETURN u
    """
    existing_tag = session.run(existing_tag_query, name=name).single()

    if existing_tag:
        return None  # User already exists
    else:
        create_query = """
        CREATE (u:Tag {name: $name})
        RETURN u
        """
        result = session.run(create_query, name=name)
        return result.single()[0]


def read_tag(session, name):
    """
    Retrieve a user node based on the email.
    :param session: Neo4j session,
    :param name: Email of the tag.
    :return: tag node or None if not found.
    """
    read_query = """
    MATCH (u:Tag {name: $name})
    RETURN u.id AS id, u.name AS name
    """
    result = session.run(read_query, name=name)
    tag = result.single()
    if tag:
        return {
            "id": tag["id"],
            "name": tag["name"],
        }
    return None


def update_tag(session, name=None):
    """
    Update a user's information.
    :param session: Neo4j session
    :param name: New name for the tag
    :return: The updated user node
    """
    update_query = """
    MATCH (u:Tag {name: $name})
    SET 
        u.name = COALESCE($name, u.name),
    RETURN u
    """
    result = session.run(update_query, name=name)
    return result.single()[0]  # Return the updated user node


def delete_tag(session, name):
    """
    Delete a user node based on the user ID.
    :param session: Neo4j session
    :param name: Unique ID of tag
    :return: True if deletion was successful, False otherwise
    """
    delete_query = """
    MATCH (u:Tag {name: $name})
    DELETE u
    RETURN COUNT(u) AS deleted_tag
    """
    result = session.run(delete_query, name=name)
    deleted_tag = result.single()["deleted_tag"]
    return deleted_tag > 0  # Returns True if deletion was successful
