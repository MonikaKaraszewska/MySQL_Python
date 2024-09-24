import mysql.connector
'''# Utwórz obiekt połączenia do bazy danych 'qatesting' o nazwie 'mydb'''
mydb = mysql.connector.connect(host='localhost', username='root', password='1234password', database = 'qatesting')

'''# Utwórz kursor do wykonywania zapytań SQL o nazwie 'mycursor'''
mycursor = mydb.cursor()


workers = [(1, 'Jan', 'Kowalski', 'jan.kowalski@example.com'),
    (2, 'Anna', 'Nowak', 'anna.nowak@example.com'),
    (3, 'Piotr', 'Wiśniewski', 'piotr.wisniewski@example.com'),
    (4, 'Katarzyna', 'Dąbrowska', 'katarzyna.dabrowska@example.com'),
    (5, 'Marek', 'Jankowski', 'marek.jankowski@example.com')]

'''umiesc dane z 'workers' w tabeli testerzy'''




'''usun baze danych qatesting (jesli nie ma dalszych cwiczen)'''

