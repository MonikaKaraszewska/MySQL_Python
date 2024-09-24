'''https://www.youtube.com/playlist?list=PLB5jA40tNf3tRMbTpBA0N7lfDZNLZAa9G'''
import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', password='1234password', database='testdb')

print(mydb)

# mojabaza=mysql.connector.connect(host='localhost', user='newuser',password='1234!@#$')
# print(mojabaza)

mycursor = mydb.cursor()

# mycursor.execute("DROP DATABASE IF EXISTS studenci")
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#     print(x)

# mycursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))")

print("show tables")
mycursor.execute("SHOW TABLES")
for tb in mycursor:
    print(tb)

