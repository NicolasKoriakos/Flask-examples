import mysql.connector

conexion = mysql.connector.connect(host='localhost', user='root', password='', database='db1')
cursor = conexion.cursor()

cursor.execute('SELECT * FROM articles')

for registro in cursor:

    print(registro)

conexion.close()