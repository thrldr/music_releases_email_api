import psycopg2
from psycopg2 import sql


class DBManager:
    '''A class resposible for managing database'''

    def __init__(self, connection_data: dict):
        self.connection = psycopg2.connect(
            database=connection_data['database'],
            user=connection_data['user'],
            password=connection_data['password'],
            host=connection_data['host'],
            port=connection_data['port'],
        )

    def fetch_all(self, table: str):
        cur = self.connection.cursor()
        query = f"SELECT * FROM {table}"
        cur.execute(query)
        data = cur.fetchall()

        cur.close()
        return data
    
    def find_by_value(self, table: str, field: str, value):
        cur = self.connection.cursor()
        query = f"SELECT * FROM {table} WHERE {field} = '{value}'"
        cur.execute(query)

        data = cur.fetchone()
        cur.close()
        return data
    
    @staticmethod
    def make_values_string(*values):
        values_string = '(DEFAULT, '
        for value in values:
            if isinstance(value, bool):
                values_string += "TRUE, "
            else:
                values_string += f"'{value}', "
        values_string = values_string[0:-2] + ')'
        return values_string

    def insert(self, table: str, *values):
        cur = self.connection.cursor()

        values_string = DBManager.make_values_string(*values)
        query = f"INSERT INTO {table} VALUES {values_string}"

        print(query)
        cur.execute(query)
        cur.close()
        self.connection.commit()
        return

    def activate(self, id: str):
        cur = self.connection.cursor()
        query = f"UPDATE users SET active = TRUE WHERE email = '{id}'"
        cur.execute(query)
        cur.close
        self.connection.commit()
    
    def deactivate(self, id: str):
        cur = self.connection.cursor()
        query = f"UPDATE users SET active = FALSE WHERE email = '{id}'"
        cur.execute(query)
        cur.close
        self.connection.commit()
