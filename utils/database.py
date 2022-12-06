from .mysrom import MySQLConnect
from os import getenv

conn = MySQLConnect(
    host = getenv('DB_HOST'),
    user = getenv('DB_USERNAME'),
    password = getenv('DB_PASSWORD'),
    database = getenv('DB_NAME')
)