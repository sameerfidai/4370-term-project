from mysql.connector import connect, Error
import os
from dotenv import load_dotenv



def dbConnection():
    load_dotenv()
    host=os.getenv('MYSQL_HOST')
    user=os.getenv('MYSQL_USER')
    password=os.getenv('MYSQL_PASSWORD')
    db=os.getenv('MYSQL_DB')
    
    try:
        with connect(
            host=host,
            user=user,
            password=password,
            db=db
        ) as connection:
            print(connection)
    except Error as e:
        print(e)
    # app.config['MYSQL_USER'] = user
    # app.config['MYSQL_PASSWORD'] = password
    # app.config['MYSQL_DB'] = db
    # mysql=MySQL(app)
    # cur=mysql.connection.cursor()