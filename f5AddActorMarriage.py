from neo4j import GraphDatabase
import pymysql

# Neo4j connection setup
neo4j_driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "neo4jneo4j"))

def actors_exist_mysql(actor1_id, actor2_id):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='appdbproj',
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT ActorID FROM actor WHERE ActorID IN (%s, %s)", (actor1_id, actor2_id))
            results = cursor.fetchall()
            return len(results) == 2
    finally:
        connection.close()

def is_actor_married(actor_id):
    with neo4j_driver.session() as session:
        result = session.run("""
            MATCH (a:Actor)-[:MARRIED_TO]-(:Actor)
            WHERE a.ActorID = $actor_id
            RETURN COUNT(*) AS count
        """, actor_id=actor_id)
        return result.single()["count"] > 0

def create_marriage_relationship(actor1_id, actor2_id):
    with neo4j_driver.session() as session:
        session.run("""
            MATCH (a1:Actor {ActorID: $actor1_id}), (a2:Actor {ActorID: $actor2_id})
            CREATE (a1)-[:MARRIED_TO]->(a2)
            CREATE (a2)-[:MARRIED_TO]->(a1)
        """, actor1_id=actor1_id, actor2_id=actor2_id)
