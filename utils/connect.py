import mysql.connector


def cnx():
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="wxl12345",
        database="mydb"
    )
    return cnx
