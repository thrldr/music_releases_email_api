import psycopg2
from psycopg2 import sql

conn = psycopg2.connect(database="mydb", user="thrldr", password="gibson777",
        host="localhost", port=5432)

cur = conn.cursor()

cur.execute("SELECT * FROM persons")
data = cur.fetchall()
print(data)

