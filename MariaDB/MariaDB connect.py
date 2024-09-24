import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user = 'root', password = '1234password', host = 'localhost', port ='3307', database = 'cas')
mycursor  = mariadb_connection.cursor()

mycursor.execute("SHOW TABLES")
for tb in mycursor:
    print(tb)

mycursor.execute("show columns in alben")
for i in mycursor:
    print(i)