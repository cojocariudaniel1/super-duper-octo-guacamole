import base64

from neo4j_data.Repository.CommunityRepository import CommunityRepository
from neo4j_data.database_connect import Neo4jDriverSingleton

if __name__== "__main__":
    Neo4jDriverSingleton(uri="bolt://localhost:7687", user="neo4j", password="12345678")
    driver = Neo4jDriverSingleton.get_driver()
    repo = CommunityRepository(driver)
    # You would typically get the base64 string from an image file
    with open(r"D:\Dizertatie proiect\super-duper-octo-guacamole\frontend\assets\images\communityIcon2.png", "rb") as image_file:
        icon_base64 = base64.b64encode(image_file.read()).decode('utf-8')
        icon_data_url = f"data:image/png;base64,{icon_base64}"

    repo.create(
        name="NewCommunity",
        description="A great new community",
        icon=icon_data_url
    )