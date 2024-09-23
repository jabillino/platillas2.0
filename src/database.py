import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="pruebav"
)

print(database, "conectado exitosamente")