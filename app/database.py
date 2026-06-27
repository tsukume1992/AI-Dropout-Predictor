import mysql.connector


def get_db_connection():

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="@May201992",
        database="project_sentinel"
    )

    return connection