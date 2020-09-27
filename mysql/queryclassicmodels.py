import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    password = "password1",
    database = "classicmodels"
)

# you have to create a cursor
cursor = db.cursor()

# define your query
query = "SELECT * FROM customers"

# execute method on cursor
cursor.execute(query)
records = cursor.fetchall()

for record in records:
    print(record)