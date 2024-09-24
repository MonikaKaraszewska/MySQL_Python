import mysql.connector
from datetime import datetime
mydb = mysql.connector.connect(host='localhost', user='root', password='1234password', database='danefirmy')

mycursor = mydb.cursor()
print('.........................ex1.....')
'''stwórz baze danych o nazwie 'danefirmy'''


print('.........................ex2....')
import datetime
'''stówrz tabele 'pracownicy' i kolumny - imie, datadzisiejasza, płec, id(ktore samo sie nadaje polokei),'''


print('.........................ex3....')
'''wprowadz dane do tabeli'''



print('.........................ex4..')
'''wyswietl tylko pracowników 'm' uporazdkowanych po id'''



print('.........................ex5..')

'''wyswetl tylko id i imie,mezczyzn posortowane według id'''



print('.........................ex5..')
'''dodaj kolumne age'''


'''dodaj kolumne food'''



'''usun kolumne food'''


'''zmien naze kolumny z age na wiek'''







print('.........................ex6..')
''''wyswietl jakie kolumny ma tabela pracownicy '''


'''ususn baze danych danefirmy'''
#
