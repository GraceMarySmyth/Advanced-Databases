from neo4j import GraphDatabase
import pymysql

def check_actor_relationship(actor_id):
    neo4j_driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "neo4jneo4j"), max_connectionLifetime=1000)
    
    with neo4j_driver.session() as session:
        result = session.run("MATCH (a:Actor)-[:married_to]-(b:Actor) WHERE a.id = $actor_id RETURN b.id, b.name", actor_id=actor_id)
        married_actors = result.data()

    return married_actors
    

conn = None

def connect():
    global conn
    try:
        mysql_conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="appdbproj",
            cursorclass=pymysql.cursors.DictCursor
        )
        cursor = mysql_conn.cursor()

        for actor in married_actors:
            cursor.execute("SELECT name FROM actors WHERE id = %s", (actor['b.id'],))
            actor_name = cursor.fetchone()
            if actor_name:
                print(f"Actor ID: {actor['b.id']}, Actor Name: {actor_name[0]}")
    finally:
        cursor.close()
        mysql_conn.close()

