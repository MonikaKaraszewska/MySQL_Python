import mysql.connector
mydb = mysql.connector.connect(host='localhost', password='1234password', user='root')

mycursor = mydb.cursor()
print("...........................................ex1")
'''utwórz baze danych o nazwie baza07'''


print('')
print("...........................................ex2..")

'''utwórz tabele o nazwie 'pracownicy' z id(ktróe samo sie nadaje), imie, nazwisko, zarobki, wiek'''


pracownicy = [("Anna", "Kowalska", 5000.00, 40),
    ("Marek", "Nowak", 6000.00, 35),
    ("Katarzyna", "Wiśniewska", 5500.00, 38),
    ("Piotr", "Lis", 7000.00, 42),
    ("Joanna", "Duda", 4800.00, 37),
    ("Grzegorz", "Mazurek", 6500.00, 39),
    ("Alicja", "Wójcik", 5200.00, 36),
    ("Marcin", "Adamczyk", 5800.00, 41),
    ("Monika", "Szymańska", 5300.00, 38),
    ("Tomasz", "Wilk", 6200.00, 40)]

print("...............................ex3")
'''wprowadz dane do tabeli pracownicy ze zeminnej 'pracownicy' i wysietl cała tabaele'''


'''wysiwetl tylko jedna osobe ktróra ma najwecej lat'''

'''wysietl sume zarobków wszytskich pracowników'''
print("...................................................................ex4")


'''wyseiwetl sume nie jako krotke tylko: Suma zarobków wszystkich pracowników: 57300.0 '''



print("..................")
print("...................................................................ex5...")
'''wysietl srednia sume zarobkow pracowników'''



print("..................count")
print("...................................................................ex5...")
'''ile jest pracowników z pensja powyzej 6000'''



print("...................................................................ex6...")
'''wysietl pracowników z zarobkami powyzej 6000'''




print("")
print("...................................................................ex7..")

print("....................min.......")
'''wyswietl osoby z minimalna i maksymalna pensja - na dwa sposoby '''



print(".........................max")


#usun baze danych jak nie ma dalszych cwiczen

