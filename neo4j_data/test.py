import base64
import uuid
from neo4j import GraphDatabase


def save_default_user_icon(driver, image_path):
    with open(image_path, 'rb') as image_file:
        encoded_icon = base64.b64encode(image_file.read()).decode('utf-8')

    icon_id = str(uuid.uuid4())

    query = """
    MERGE (icon:UserIconDefault {id: $id})
    SET icon.image = $image
    RETURN icon
    """
    with driver.session() as session:
        result = session.run(query, id=icon_id, image=encoded_icon)
        saved_icon = result.single()[0]
        print(f"Icon saved with ID: {icon_id}")
        return saved_icon


# Exemplu de utilizare:
if __name__ == "__main__":
    from neo4j import GraphDatabase

    # Înlocuiește cu detaliile tale de conexiune
    URI = "bolt://localhost:7687"
    USER = "neo4j"
    PASSWORD = "12345678"

    driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))

    icon_path = "default_icon.png"  # Calea către fișierul PNG
    save_default_user_icon(driver, icon_path)

    driver.close()
