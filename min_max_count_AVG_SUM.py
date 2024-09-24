import mysql.connector
mydb = mysql.connector.connect(host='localhost', password='1234password', user='root', database='mojafirma')

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM pracownicy WHERE zarobki < 6200")
# coto = mycursor.fetchall()
# print("coto" , coto[4])
for i in mycursor:
    print(i)
print('')
print("..................sum")
mycursor.execute("SELECT SUM(zarobki) FROM pracownicy")
efekt = mycursor.fetchone()
suma=efekt[0]
print(suma)
# for i in mycursor:
#     print(i)


# mycursor.execute("SELECT SUM(zarobki) FROM pracownicy")
# result = mycursor.fetchone()
# suma_zarobkow = result[0]
# print("Suma zarobków wszystkich pracowników: {}".format(suma_zarobkow))
print("..................avg")
mycursor.execute("SELECT AVG(zarobki) FROM pracownicy")
efekt = mycursor.fetchone()
suma=efekt[0]
print(suma)

print("..................count")

mycursor.execute("SELECT count(zarobki) FROM pracownicy where zarobki>6000")
efekt = mycursor.fetchone()
suma=efekt[0]
print(suma)

mycursor.execute("SELECT * FROM pracownicy where zarobki>6000")
for i in mycursor:
    print(i)

print("....................min........max")
# wyswietla to jako krotka
# zeby wysietlilonormalnie, trzeba wynik zapisac do zmiennej a potem
mycursor.execute("SELECT min(zarobki) from pracownicy")
for i in mycursor:
    print(i)

mycursor.execute("SELECT max(zarobki) from pracownicy")
for i in mycursor:
    print(i)

# zeby wysietlilonormalnie, trzeba wynik zapisac do zmiennej a potem wydrukowac indeks 0, jako ze jest to krotka z jednym elelementem
mycursor.execute("SELECT max(zarobki) from pracownicy")
wynik = mycursor.fetchone()
print(wynik[0])