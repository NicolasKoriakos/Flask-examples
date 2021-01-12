import mysql.connector

conexion = mysql.connector.connect(host='localhost', user='root', password='', database='db1')
cursor = conexion.cursor()



# cursor.execute('show tables')

# for db in cursor:

#     print(db)

sql = 'INSERT INTO articles (item, price) values (%s, %s)'
datos = ('PEAR', 1.99)

cursor.execute(sql, datos)

conexion.commit()
conexion.close()