import mysql.connector
'''# Utwórz obiekt połączenia do bazy danych 'qatesting' o nazwie 'mydb'''
mydb = mysql.connector.connect(host='localhost', user='root', password='1234password', port ='3307',database='qatesting')
print(mydb)

'''# Utwórz kursor do wykonywania zapytań SQL o nazwie 'mycursor'''
mycursor = mydb.cursor()
# mycursor.execute("SHOW COlUMNS in testerzy")
# for tb in mycursor:
#     print(tb)
# #
# workers = [(1, 'Jan', 'Kowalski', 'jan.kowalski@example.com'),
#     (2, 'Anna', 'Nowak', 'anna.nowak@example.com'),
#     (3, 'Piotr', 'Wisniewski', 'piotr.wisniewski@example.com'),
#     (4, 'Katarzyna', 'Dabrowska', 'katarzyna.dabrowska@example.com'),
#     (5, 'Marek', 'Jankowski', 'marek.jankowski@example.com')]
#
# '''umiesc dane z 'workers' w tabeli testerzy'''
# myzor = "INSERT INTO testerzy (id, name, nazwisko, adres_email) VALUES (%s, %s, %s, %s)"
# mycursor.executemany(myzor,workers)
# mydb.commit()

'''usun baze danych qatesting'''
# mycursor.execute("DROP DATABASE IF EXISTS qatesting")
# mydb.commit()

mycursor.execute('create table points (id_p int,foreign key (id_p) references testerzy (id), punkty int')
