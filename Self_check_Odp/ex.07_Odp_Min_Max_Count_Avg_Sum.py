import mysql.connector
mydb = mysql.connector.connect(host='localhost', password='1234password', user='root', database='baza_ex07')

mycursor = mydb.cursor()
print("...........................................ex1")
'''utwórz baze danych o nazwie baza07'''
# mycursor.execute("CREATE database baza_ex07")
# mydb.commit()
print('')
print("...........................................ex2..")

'''utwórz tabele o nazwie 'pracownicy' z id(ktróe samo sie nadaje), imie, nazwisko, zarobki, wiek'''

# mycursor.execute("Create table pracownicy (id int primary key auto_increment, imie VARCHAR(50), nazwisko VARCHAR(50), zarobki float, wiek int)")
# mydb.commit()

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
# dane = "INSERT INTO pracownicy (imie, nazwisko, zarobki, wiek) VALUES(%s,%s,%s,%s)"
# mycursor.executemany(dane,pracownicy)
# mydb.commit()

mycursor.execute("Select * from pracownicy")
for i in mycursor:
    print(i)

'''wysietl sume zarobków wszytskich pracowników'''
print("...................................................................ex4")
mycursor.execute("SELECT SUM(zarobki) FROM pracownicy zarobki")
for i in mycursor:
    print(i)

'''wyseiwetl sume nie jako krotke tylko: Suma zarobków wszystkich pracowników: 57300.0 '''
mycursor.execute("SELECT SUM(zarobki) FROM pracownicy")
result = mycursor.fetchone()
suma_zarobkow = result[0]
print("Suma zarobków wszystkich pracowników: {}".format(suma_zarobkow))


print("..................")
print("...................................................................ex5...")
'''wysietl srednia sume zarobkow pracowników'''
mycursor.execute("SELECT AVG(zarobki) FROM pracownicy")
efekt = mycursor.fetchone()
suma=efekt[0]
print(suma)

print("..................count")
print("...................................................................ex5...")
'''ile jest pracowników z pensja powyzej 6000'''
mycursor.execute("SELECT count(zarobki) FROM pracownicy where zarobki>6000")
efekt = mycursor.fetchone()
suma=efekt[0]
print(suma)
print("...................................................................ex6...")
'''wysietl pracowników z zarobkami powyzej 6000'''
mycursor.execute("SELECT * FROM pracownicy where zarobki>6000")
for i in mycursor:
    print(i)
print("")
print("...................................................................ex7..")

print("....................min.......")
'''wyswietl osoby z minimalna i maksymalna pensja - na dwa sposoby '''


mycursor.execute("SELECT imie, nazwisko, zarobki FROM pracownicy WHERE zarobki = (SELECT MIN(zarobki) FROM pracownicy)")
for i in mycursor:
    print(i)

print('albo')
mycursor.execute("SELECT imie, nazwisko, zarobki FROM pracownicy ORDER BY zarobki ASC LIMIT 1")
for i in mycursor:
    print(i)


print(".........................max")

mycursor.execute("SELECT max(zarobki) from pracownicy")
for i in mycursor:
    print(i)

# zeby wysietlilonormalnie, trzeba wynik zapisac do zmiennej a potem wydrukowac indeks 0, jako ze jest to krotka z jednym elelementem
mycursor.execute("SELECT max(zarobki) from pracownicy")
wynik = mycursor.fetchone()
print(wynik[0])