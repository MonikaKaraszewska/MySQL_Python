'''https://www.youtube.com/playlist?list=PLB5jA40tNf3tRMbTpBA0N7lfDZNLZAa9G'''

import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', password='1234password', database='qatesting')
print(mydb)

mycursor = mydb.cursor()

mycursor.execute('SELECT* FROM testerzy')
myresult = mycursor.fetchall()
for i in myresult:
    print(i)

mycursor.execute('SELECT imie FROM testerzy')
myresult = mycursor.fetchall()
for i in myresult:
    print(i)
print('  ')
#fetchone - pokazuje pierwszy wpis
mycursor.execute('SELECT nazwisko FROM testerzy')
myresult = mycursor.fetchone()
for i in myresult:
    print(i)

