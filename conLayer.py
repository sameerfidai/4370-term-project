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


# query 1
def query1(month):
    try:
        args=[month]
        connection = dbConnection()
        cursor = connection.cursor()
        cursor.callproc('Query1',args)
        for i in cursor.stored_results():
            return list(i.fetchall())
    except Exception as e:
        print(e)


# query2 need to figure out how to send inputs from flask server and
def query2(year1, year2):
    try:
        args = [year1, year2]
        connection = dbConnection()
        cursor = connection.cursor()
        cursor.callproc('Query2', args)
        for i in cursor.stored_results():
            return list(i.fetchall())
    except Exception as e:
        print(e)


# query 3
def query3(dirname1):
    try:
        # print("Ran query3")
        # print(dirname1)
        # print(dirname2)
        results = 0
        tconst = ""
        args = [dirname1]
        connection = dbConnection()
        cursor = connection.cursor()
        cursor.callproc('Query3', args)
        for i in cursor.stored_results():
            # return str(i.fetchall())
            for x in i.fetchall():

                tconst = x[0]

        tconstData = tconst.split(",")
        tconstData = tconstData[:-1]
        title = tconstData[0]
        title2 = tconstData[1]
        title3 = tconstData[2]
        args2 = [title, title2, title3]
        cursor.callproc('findGenre', args2)
        for x in cursor.stored_results():
            # return str(i.fetchall())

            return list(x.fetchall())
    except Exception as e:
        print(e)


# query4
def query4(dirname1):
    try:
        # print("Ran query3")
        # print(dirname1)
        # print(dirname2)
        results = 0
        tconst = ""
        args = [dirname1]
        connection = dbConnection()
        cursor = connection.cursor()
        cursor.callproc('Query3', args)
        for i in cursor.stored_results():
            # return str(i.fetchall())
            for x in i.fetchall():

                tconst = x[0]

        tconstData = tconst.split(",")
        tconstData = tconstData[:-1]
        title = tconstData[0]
        title2 = tconstData[1]
        title3 = tconstData[2]
        args2 = [title, title2, title3]
        cursor.callproc('Query4', args2)
        for x in cursor.stored_results():
            # return str(i.fetchall())

            return list(x.fetchall())

    except Exception as e:
        print(e)


# query5
def query5(year1, year2, gen):
    try:
        args = [year1, year2, gen]
        connection = dbConnection()
        cursor = connection.cursor()
        cursor.callproc('Query5', args)
        for i in cursor.stored_results():
            # return str(i.fetchall())
            return list((i.fetchall()))
    except Exception as e:
        print(e)
