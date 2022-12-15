from mysql.connector import connect, Error
import os
from dotenv import load_dotenv


def dbConnection():
    load_dotenv()
    host = os.getenv('MYSQL_HOST')
    user = os.getenv('MYSQL_USER')
    password = os.getenv('MYSQL_PASSWORD')
    db = os.getenv('MYSQL_DB')

    connection = connect(
        host=host,
        user=user,
        password=password,
        db=db
    )

    # app.config['MYSQL_USER'] = user
    # app.config['MYSQL_PASSWORD'] = password
    # app.config['MYSQL_DB'] = db
    # mysql=MySQL(app)
    # cur=mysql.connection.cursor()
    return connection


def query1():
    try:
        connection = dbConnection()
        cursor = connection.cursor()
        cursor.callproc('Query1')
        for i in cursor.stored_results():
            return str(i.fetchall())
    except Exception as e:
        print(e)
