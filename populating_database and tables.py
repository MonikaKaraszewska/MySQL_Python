'''https://www.youtube.com/playlist?list=PLB5jA40tNf3tRMbTpBA0N7lfDZNLZAa9G'''
import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', password='1234password', database='testdb')

print(mydb)
mycursor = mydb.cursor()
sqlFormula = "INSERT INTO students (name,age) VALUES (%s, %s)"

students = [("Anna", 88),
            ("JAke", 67),
            ("Bond", 40),
            ("Batman", 99),
            ("Asia", 15),
            ("Pawcio", 8)]


mycursor.executemany(sqlFormula, students)

# mydb.commit()
workers = [(1, 'Jan', 'Kowalski', 'jan.kowalski@example.com', 25, '2023-01-01'),
    (2, 'Anna', 'Nowak', 'anna.nowak@example.com', 30, '2023-02-15'),
    (3, 'Piotr', 'Wiśniewski', 'piotr.wisniewski@example.com', 22, '2023-03-10'),
    (4, 'Katarzyna', 'Dąbrowska', 'katarzyna.dabrowska@example.com', 28, '2023-04-22'),
    (5, 'Marek', 'Jankowski', 'marek.jankowski@example.com', 35, '2023-05-05')]