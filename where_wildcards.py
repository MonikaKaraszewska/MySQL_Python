'''https://www.youtube.com/watch?v=OTzL0oH-ZGI&list=PLB5jA40tNf3tRMbTpBA0N7lfDZNLZAa9G&index=5'''

import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root',password='1234password',database='qatesting')

mycursor=mydb.cursor()

'''tworze polecenie w dodzielnej zmiennej'''
sglcommand = "SELECT * FROM testerzy WHERE imie = 'Anna'"
mycursor.execute(sglcommand)

wyniksqlcommand = mycursor.fetchall()

for wynik in wyniksqlcommand:
    print(wynik)
print('')
print(".......................wildcard .........characters.....................")
'''co oznacza %'''
sglcommand = "SELECT * FROM testerzy WHERE imie LIKE '%an%'"
# sglcommand = "SELECT * FROM testerzy WHERE imie LIKE 'an%'"
# sglcommand = "SELECT * FROM testerzy WHERE imie LIKE 'An%'"


mycursor.execute(sglcommand)

wyniksqlcommand = mycursor.fetchall()

for wynik in wyniksqlcommand:
    print(wynik)