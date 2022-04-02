from os import getenv

connection_data = {
    "database": getenv('DATABASE'),
    "user": getenv('USERNAME'),
    "password": getenv('PASSWORD'),
    "host": getenv('HOST'),
    "port": getenv('PORT')
}

