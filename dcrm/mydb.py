import mysql.connector

# Create a database connection
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'super',
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create the database
cursorObject.execute("CREATE DATABASE crm_db")

print("All Done Successfully!")