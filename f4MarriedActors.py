from neo4j import GraphDatabase
import pymysql

class F4MarriedActors:
    def __init__(self):
        self.neo4j_driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "neo4jneo4j"))

    def check_actor_relationship(self, actor_id):
        with self.neo4j_driver.session() as session:
            result = session.run("""
                MATCH (a:Actor {ActorID: $actor_id})-[:MARRIED_TO]-(b:Actor)
                RETURN b.ActorID AS partner_id
            """, actor_id=actor_id)
            data = [record["partner_id"] for record in result]
            return data

    def connect(self, actor_ids):
        try:
            mysql_conn = pymysql.connect(
                host="localhost",
                user="root",
                password="root",
                database="appdbproj",
                cursorclass=pymysql.cursors.DictCursor
            )
            with mysql_conn.cursor() as cursor:
                placeholders = ','.join(['%s'] * len(actor_ids))
                query = f"SELECT ActorID, ActorName FROM actor WHERE ActorID IN ({placeholders})"
                cursor.execute(query, tuple(actor_ids))
                results = cursor.fetchall()

            if results:
                for actor in results:
                    print("---------------------------")
                    print("These actors are Married:")
                    print(f"Actor ID: {actor['ActorID']}, Actor Name: {actor['ActorName']}")
            else:
                print("This actor is not married.")
        
        except Exception as e:
            print("Database error:", e)
        finally:
            mysql_conn.close()
