import mysql.connector
from datetime import datetime
mydb = mysql.connector.connect(host='localhost', user='root', password='1234password')

mycursor = mydb.cursor()
print('.........................ex1.....')
'''stwórz baze danych o nazwie 'danefirmy'''
# mycursor.execute("CREATE DATABASE danefirmy")
# mydb.commit()
print('.........................ex2....')

'''stówrz tabele 'pracownicy' i kolumny - imie, datadzisiejasza, płec, id(ktore samo sie nadaje polokei),'''
# mycursor.execute("CREATE TABLE pracownicy (name VARCHAR(50) NOT NULL, created datetime NOT NULL, gender ENUM('M', 'F', 'O') NOT NULL, id int PRIMARY KEY NOT NULL  AUTO_INCREMENT)")
print('.........................ex3....')
'''wprowadz dane do tabeli'''

# mycursor.execute("Insert into pracownicy (name,created,gender) VALUES (%s,%s,%s)",('Ann',datetime.now(), 'F'))
# mydb.commit()
print('.........................ex4..')
'''wyswietl tylko pracowników 'm' uporazdkowanych po id'''

# mycursor.execute("Select* from pracownicy where gender='M' order by id")
# for i in mycursor:
#     print(i)
#
print('.........................ex5..')

'''wyswetl tylko id i imie,mezczyzn posortowane według id'''
# mycursor.execute("Select id, name from pracownicy where gender='M' order by id")
# for i in mycursor:
#     print(i)
print('.........................ex5..')
'''dodaj kolumne age'''
# mycursor.execute("AlTER TABLE pracownicy ADD COLUMN age varchar(50) not null")

'''dodaj kolumne food'''
# mycursor.execute("AlTER TABLE pracownicy ADD COLUMN food varchar(50) not null")

'''usun kolumne food'''
# mycursor.execute("ALTER TABLE pracownicy DROP food")

'''zmien naze kolumny z age na wiek'''
# mycursor.execute("ALTER TABLE pracownicy change age wiek varchar(50)")

print('.........................ex6..')
''''wyswietl jakie kolumny ma tabela pracownicy '''
# mycursor.execute("DESCRIBE pracownicy")
# for i in mycursor:
#     print(i)

'''ususn baze danych danefirmy'''
# mycursor.execute("DROP database if exists ramzes")
# mydb.commit()
