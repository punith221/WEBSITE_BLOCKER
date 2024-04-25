import mysql.connector

db_host = "localhost"
db_user = "root"
db_password = ""  # database password
db_name = "websiteblocker"  # create database named "websiteblocker"


def get_db_connection():
    return mysql.connector.connect(
        host=db_host,
        user=db_user,
        passwd=db_password,
        database=db_name
    )


def close_db_connection(cursor, connection):
    connection.commit()
    cursor.close()
    connection.close()


def db_write(cursor, query, values):
    cursor.execute(query, values)
