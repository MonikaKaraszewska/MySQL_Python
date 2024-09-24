'''https://www.youtube.com/playlist?list=PLB5jA40tNf3tRMbTpBA0N7lfDZNLZAa9G'''
'''# połacz się z baza danych qatesting, i utwórz swójłacznik do komunikowania sie i wykonywania polecen na bazie danych  '''

import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', password='1234password', database='qatesting')
mycursor = mydb.cursor()
print('.................ex1.....')
'''wyswietl cała tablice testerzy'''
mycursor.execute('SELECT* FROM testerzy')
myresult = mycursor.fetchall()
for i in myresult:
    print(i)
print('....................ex.2')
'''wyswietl tylko imiona z tablicy testerzy'''
mycursor.execute('SELECT imie FROM testerzy')
myresult = mycursor.fetchall()
for i in myresult:
    print(i)
print('....................................ex.3')

'''tworze polecenie w dodzielnej zmiennej'''
sglcommand = "SELECT * FROM testerzy WHERE imie = 'Anna'"
mycursor.execute(sglcommand)

wyniksqlcommand = mycursor.fetchall()

for wynik in wyniksqlcommand:
    print(wynik)
print('')
print("....................exercise4...................")
'''co oznacza %'''
# wyswietl imiona które zaczynaja sie na 'an'
sglcommand = "SELECT * FROM testerzy WHERE imie LIKE 'an%'"

# wyswietl nazwiska które koncza sie na 'ski'
sglcommand = "SELECT * FROM testerzy WHERE nazwisko LIKE '%ski'"

# wyswietl nazwiska które maja w sobie 'ow'
sglcommand = "SELECT * FROM testerzy WHERE nazwisko LIKE '%ow%'"

mycursor.execute(sglcommand)
wyniksqlcommand = mycursor.fetchall()
for wynik in wyniksqlcommand:
    print(wynik)
