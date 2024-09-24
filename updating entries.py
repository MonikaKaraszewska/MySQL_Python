'''https://www.youtube.com/watch?v=OTzL0oH-ZGI&list=PLB5jA40tNf3tRMbTpBA0N7lfDZNLZAa9G&index=5'''

import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root',password='1234password',database='qatesting')

mycursor=mydb.cursor()

# '''tworze polecenie w dodzielnej zmiennej'''
# polcenie = "UPDATE testerzy SET adres_email='nowak@gmail.com' Where imie='Anna'"
#
# mycursor.execute(polcenie)
# mydb.commit()
print('')
print(".................................................NOT....IN ")
polecenie2 = "SELECT * FROM testerzy WHERE imie NOT IN ('Anna','Jan')"
mycursor.execute(polecenie2)
efekt = mycursor.fetchall()

for i in efekt:
    print(i)
print('')
print(".....................................................IN ")
polecenie2 = "SELECT * FROM testerzy WHERE imie IN ('Anna','Jan')"
mycursor.execute(polecenie2)
efekt = mycursor.fetchall()
for i in efekt:
    print(i)

print('...usun')
# usun adres emial
usun = "UPDATE testerzy SET adres_email= null WHERE imie = 'Anna'"
mycursor.execute(usun)
mydb.commit()
print('')
print('??')
polecenie2 = "SELECT * FROM testerzy WHERE adres_email IS not NULL"
mycursor.execute(polecenie2)
efekt = mycursor.fetchall()
for i in efekt:
    print(i)

print('')
print('.....limiting queries')
'''wysietli 5 pierwszych'''
mycursor.execute("SELECT * FROM testerzy LIMIT 5")
myresult = mycursor.fetchall()
for i in myresult:
    print(i)
print('')
'''wysietli 5 ale zprzedzału ktory podam NP od 2-go wpisu'''
mycursor.execute("SELECT * FROM testerzy LIMIT 5 OFFSET 2")
myresult = mycursor.fetchall()
for i in myresult:
    print(i)