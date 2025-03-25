import uuid  # For generating unique community IDs


class CommunityRepository:
    def __init__(self, driver):
        self.driver = driver

    def create(self, name, description, privacy_level="public", reputation_required=0, banner_image=None):
        print(f"Debug: Creating community '{name}' with privacy level '{privacy_level}'")
        return create_community(self.driver, name, description, privacy_level, reputation_required, banner_image)

    def read(self, community_name):
        community = read_community(self.driver, community_name)
        if community:
            print(f"Debug: Retrieved community '{community['name']}'")
        return community

    def update(self, name=None, description=None, privacy_level=None, reputation_required=None, banner_image=None):
        return update_community(self.driver, name, description, privacy_level, reputation_required, banner_image)

    def delete(self, name):
        return delete_community(self.driver, name)





def create_community(driver, name, description, privacy_level, reputation_required, banner_image):
    """
    Create a new community node in the Neo4j database if a community with the same name doesn't already exist.
    :param driver: Neo4j driver instance
    :param name: Name of the community
    :param description: Description of the community
    :param privacy_level: Privacy level of the community (default: "public")
    :param reputation_required: Minimum reputation required to join (default: 0)
    :param banner_image: URL for the community's banner image (optional)
    :return: The created community node or None if the community already exists
    """
    with driver.session() as session:
        with session.begin_transaction() as tx:
            # Check if a community with the same name already exists
            existing_community_query = """
            MATCH (c:Community {name: $name})
            RETURN c
            """
            existing_community = tx.run(existing_community_query, name=name).single()

            if existing_community:
                print("Community already exists")
                return None  # Community already exists
            else:
                create_query = """
                CREATE (c:Community {
                    id: $id,
                    name: $name,
                    description: $description,
                    privacy_level: $privacy_level,
                    reputation_required: $reputation_required,
                    banner_image: $banner_image,
                    created_at: timestamp()
                })
                RETURN c
                """
                community_id = str(uuid.uuid4())  # Generate a unique ID
                result = tx.run(create_query, id=community_id, name=name, description=description,
                                privacy_level=privacy_level, reputation_required=reputation_required, banner_image=banner_image)
                return result.single()[0]


def read_community(driver, community_name):
    """
    Retrieve a community node based on the community name.
    :param driver: Neo4j driver instance
    :param community_name: Name of the community
    :return: The community node or None if not found
    """
    with driver.session() as session:
        with session.begin_transaction() as tx:
            read_query = """
            MATCH (c:Community {name: $community_name})
            RETURN c.id AS id, c.name AS name, c.description AS description,
                   c.privacy_level AS privacy_level, c.reputation_required AS reputation_required,
                   c.banner_image AS banner_image, c.created_at AS created_at
            """
            result = tx.run(read_query, community_name=community_name)
            community = result.single()
            if community:
                return {
                    "id": community["id"],
                    "name": community["name"],
                    "description": community["description"],
                    "privacy_level": community["privacy_level"],
                    "reputation_required": community["reputation_required"],
                    "banner_image": community["banner_image"],
                    "created_at": community["created_at"],
                }
            return None


def update_community(driver, name=None, description=None, privacy_level=None, reputation_required=None, banner_image=None):
    """
    Update a community's information.
    :param driver: Neo4j driver instance
    :param name: New name for the community (optional)
    :param description: New description for the community (optional)
    :param privacy_level: New privacy level for the community (optional)
    :param reputation_required: New reputation required for the community (optional)
    :param banner_image: New banner image URL for the community (optional)
    :return: The updated community node or None if not found
    """
    with driver.session() as session:
        with session.begin_transaction() as tx:
            update_query = """
            MATCH (c:Community {name: $name})
            SET 
                c.name = COALESCE($name, c.name),
                c.description = COALESCE($description, c.description),
                c.privacy_level = COALESCE($privacy_level, c.privacy_level),
                c.reputation_required = COALESCE($reputation_required, c.reputation_required),
                c.banner_image = COALESCE($banner_image, c.banner_image)
            RETURN c
            """
            result = tx.run(update_query, name=name, description=description,
                            privacy_level=privacy_level, reputation_required=reputation_required,
                            banner_image=banner_image)

            # Check if the result has a value
            record = result.single()
            if record:
                return record["c"]  # Return the community node
            else:
                print(f"Debug: No community found with the name {name}")
                return None


def delete_community(driver, name):
    """
    Delete a community node based on the community name.
    :param driver: Neo4j driver instance
    :param name: Name of the community
    :return: True if deletion was successful, False otherwise
    """
    with driver.session() as session:
        with session.begin_transaction() as tx:
            delete_query = """
            MATCH (c:Community {name: $name})
            DELETE c
            RETURN COUNT(c) AS deleted_count
            """
            result = tx.run(delete_query, name=name)
            deleted_count = result.single()["deleted_count"]
            return deleted_count > 0  # Returns True if deletion was successful