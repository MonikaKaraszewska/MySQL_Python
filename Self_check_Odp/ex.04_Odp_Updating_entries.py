
import mysql.connector
'''# połacz się z baza danych qatesting, i utwórz swójłacznik do komunikowania sie i wykonywania polecen na bazie danych  '''

mydb = mysql.connector.connect(host='localhost', user='root',password='1234password',database='qatesting')

mycursor=mydb.cursor()
print("................................................ex1 ")

'''tworze polecenie w dodzielnej zmiennej'''
#utwórz polecenie zeby adres emial Pani Ani zmieniony został na 'nowak@gmail.com
polcenie = "UPDATE testerzy SET adres_email='nowak@gmail.com' Where imie='Anna'"
mycursor.execute(polcenie)
mydb.commit()

print('')
print(".................................................ex2")
# wysietl wszytkich poza tymi co maja na imie Anna albo JAn
polecenie2 = "SELECT * FROM testerzy WHERE imie NOT IN ('Anna','Jan')"
mycursor.execute(polecenie2)
efekt = mycursor.fetchall()
for i in efekt:
    print(i)
print('')
print(".............................................ex.3...... ")
# wysietl wszystkich o imionach Anna i Jan
polecenie2 = "SELECT * FROM testerzy WHERE imie IN ('Anna','Jan')"
mycursor.execute(polecenie2)
efekt = mycursor.fetchall()
for i in efekt:
    print(i)

print('')
print('.....................ex4..')
'''wysietli 5 pierwszych wpisow'''
mycursor.execute("SELECT * FROM testerzy LIMIT 5")
myresult = mycursor.fetchall()
for i in myresult:
    print(i)
print('')
print('.....................ex5..')

'''wysietli 5 ale zprzedzału ktory podam od 2-go wpisu'''
mycursor.execute("SELECT * FROM testerzy LIMIT 5 OFFSET 2")
myresult = mycursor.fetchall()
for i in myresult:
    print(i)

print('................order by')
mycursor.execute("select * from testerzy order by imie desc")
for i in mycursor:
    print(i)