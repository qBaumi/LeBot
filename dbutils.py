import mysql.connector
from config import dbargs


def sql_exec(sql):
    """
        W3SCHOOLS MYSQL CONNECTOR FOR MOR INFO
    """
    mydb = mysql.connector.connect(
        host=dbargs["host"],
        user=dbargs["user"],
        password=dbargs["password"],
        port=dbargs["port"],
        database=dbargs["database"],
        auth_plugin=dbargs["auth_plugin"]

    )
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    mydb.commit()
    mycursor.close()
    mydb.close()
def sql_select(sql):
    mydb = mysql.connector.connect(
        host=dbargs["host"],
        user=dbargs["user"],
        password=dbargs["password"],
        port=dbargs["port"],
        database=dbargs["database"],
        auth_plugin=dbargs["auth_plugin"]

    )
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    data = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return data
