import mysql.connector
'''# Utwórz obiekt połączenia do bazy danych o nazwie 'myconnect'''
myconnect = mysql.connector.connect(host='localhost', user='root', password='1234password', port ='3307', database='qatesting')

# print(myconnect)
#
# '''# Utwórz kursor do wykonywania zapytań SQL o nazwie 'pilot'''
pilot = myconnect.cursor()
# '''# utworz baze danych o nazwie QAtesting'''
# pilot.execute('drop DATABASE if exists QAtesting ')
# pilot.execute('CREATE DATABASE QAtesting ')
# '''#Wyswietl dostepne bazy danych'''
# pilot.execute("SHOW DATABASES")
# for x in pilot:
#     print(x)
# '''w bazie danych 'qatesting' utwórz tabele  o nazwie testerzy i 4 kolumnami, id, imie, nazwisko, adres_email'''
# pilot.execute("CREATE TABLE testerzy (id  VARCHAR(100) primary key,name VARCHAR(255), nazwisko VARCHAR(255), adres_email VARCHAR(255))")
#
# print("...............................show tables")
# '''#wyswietl tabele w bazie danych qatesting'''
# pilot.execute("SHOW TABLES")
# for tb in pilot:
#     print(tb)
#
# print("................................show ..columns")
# '''##wyswietl kolumny z tabeli testerzy'''
pilot.execute("SHOW COlUMNS in testerzy")
for tb in pilot:
    print(tb)


