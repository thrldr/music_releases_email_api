import psycopg2
from psycopg2 import sql
import os

class DBManager:
    connection = psycopg2.connect(
            database=os.getenv('DATABASE'),
            user=os.getenv('USERNAME'),
            password=os.getenv('PASSWORD'),
            host=os.getenv('HOST'),
            port=os.getenv('PORT')
        )

    @classmethod
    def fetch_all(cls, table: str):
        cur = cls.connection.cursor()

        query = f"SELECT * FROM {table}"
        cur.execute(query)

        data = cur.fetchall()
        cur.close()

        return data
    
    @classmethod
    def find_by_value(cls, table, field, value):
        cur = cls.connection.cursor()

        query = f"SELECT * FROM {table} WHERE {field} = '{value}'"
        cur.execute(query)

        data = cur.fetchone()
        cur.close()

        return data
    
    @staticmethod
    def make_values_string(*values):
        values_string = '(DEFAULT, '
        for value in values:
            values_string += f"'{value}', "
        values_string = values_string[0:-2] + ')'
        return values_string

    @classmethod
    def insert(cls, table, *values):
        cur = cls.connection.cursor()

        values_string = DBManager.make_values_string(*values)
        query = f"INSERT INTO {table} VALUES {values_string}"

        print(query)
        cur.execute(query)
        cur.close()
        DBManager.connection.commit()
        return
