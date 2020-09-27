import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    password = "password1"
)

print(db)

cursor = db.cursor()

cursor.execute("SHOW DATABASES")
databases = cursor.fetchall()
print(databases)
