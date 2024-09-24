import mysql.connector
mydb = mysql.connector.connect(host='localhost', password='1234password', user='root', database='mojafirma')

mycursor = mydb.cursor()

# mycursor.execute("CREATE database mojafirma")
# mydb.commit()

# mycursor.execute("Create table mentorzy (id int primary key auto_increment, imie VARCHAR(50), nazwisko VARCHAR(50), dataPrzyjecia VARCHAR(50), adresEmail  VARCHAR(50), nrTelefonu VARCHAR(50))")
# mydb.commit()

mentorzy = [('Anna', 'Nowak', '2023-01-15', 'anna.nowak@example.com', '123-456-789'),
('Marek', 'Kowalski', '2023-02-05', 'marek.kowalski@example.com', '987-654-321'),
('Katarzyna', 'Duda', '2023-03-20', 'katarzyna.duda@example.com', '111-222-333'),
('Piotr', 'Lis', '2023-04-10', 'piotr.lis@example.com', '444-555-666'),
('Joanna', 'Mazurek', '2023-05-08', 'joanna.mazurek@example.com', '777-888-999'),
('Grzegorz', 'Wójcik', '2023-06-25', 'grzegorz.wojcik@example.com', '333-222-111'),
('Alicja', 'Adamczyk', '2023-07-12', 'alicja.adamczyk@example.com', '999-888-777'),
('Marcin', 'Kaczmarek', '2023-08-30', 'marcin.kaczmarek@example.com', '666-555-444'),
('Monika', 'Szymańska', '2023-09-18', 'monika.szymanska@example.com', '222-333-444'),
('Tomasz', 'Wilk', '2023-10-05', 'tomasz.wilk@example.com', '555-444-333')]

# q1 = "Insert into mentorzy (imie, nazwisko, dataPrzyjecia, adresEmail, nrTelefonu) Values(%s, %s,%s,%s,%s)"
# mycursor.executemany(q1,mentorzy)
# mydb.commit()

# q2 = "CREATE table scores (userId int primary key, foreign key(userId) references users(id),  game1 int DEFAULT 0,  game2 int DEFAULT 0)"
q22 = "Create table pracownicy (userId int primary key auto_increment, imie VARCHAR(50), nazwisko VARCHAR(50), zarobki VARCHAR(50), czas_pracy VARCHAR(50), mentor int, foreign key(mentor) references mentorzy(id))"
# mycursor.execute(q22)
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

q3="Insert into pracownicy (imie, nazwisko, zarobki, czas_pracy) VALUES (%s,%s,%s, %s)"

# mycursor.executemany(q3,pracownicy)
# mydb.commit()
# mycursor.execute('ALTER TABLE pracownicy ADD COLUMN created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP')

# mycursor.execute("insert into pracownicy (imie, nazwisko,zarobki,czas_pracy) Values ('tomek','falbowski', 78000.00, 34)")

# mycursor.execute("update pracownicy set imie='TOMEK' where imie='tomek'")
# mydb.commit()


