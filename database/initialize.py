from os import getenv
from database.dbmanager import DBManager


connection_data = {
    "database": getenv('DATABASE'),
    "user": getenv('USERNAME'),
    "password": getenv('PASSWORD'),
    "host": getenv('HOST'),
    "port": getenv('PORT')
}

db = DBManager(connection_data)
