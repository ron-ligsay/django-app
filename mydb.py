import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user = "root",
    passwd = "charlotte"
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE dcrm_db")

print("Database created successfully")