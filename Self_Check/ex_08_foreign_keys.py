import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', password='1234password', database='moje_dane')

mycursor = mydb.cursor()
''' utworz baze danych moje_dane'''
# mycursor.execute("CREATE DATABASE moje_dane")
# mydb.commit()

users_data= [('Anna','haslo123', 'anna@example.com'),
('Marek', 'securepass', 'marek@example.com'),
('Katarzyna', 'password123', 'kasia@example.com'),
('Piotr','pass1234', 'piotr@example.com'),
('Joanna', 'userpass', 'joanna@example.com'),
('Grzegorz', 'grzpass', 'grzegorz@example.com'),
('Alicja', 'alicja123', 'alicja@example.com'),
('Marcin', 'marcinpass', 'marcin@example.com'),
('Monika', 'monikapass', 'monika@example.com'),
('Tomasz', 'tomekpass', 'tomasz@example.com')]

user_scores = [(45,100),(34,500),(56,700),(23,577),(34,788),(78,999), (47,679),(49,245),(67,348),(12,300)]
'''utwórz tabele useres z id(ktre samo sie nadaje), imie, password, email, data dzisiejsza'''
q1 = "Create table users (id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), password VARCHAR(50))"

'''utworz tabele scores z 3 kolumnami (id-primary key,który jest tez foreign key z tableki users(id), game1, game2)'''
q2 = "CREATE table scores (userId int primary key, foreign key(userId) references users(id),  game1 int DEFAULT 0,  game2 int DEFAULT 0)"
#
# mycursor.execute(q1)
# mycursor.execute(q2)

'''pokaz wszytskie tabele'''
# mycursor.execute("Describe users")
# mycursor.execute("Show tables")
mycursor.execute("Select distinct name from users")
for i in mycursor:
    print(i)

'''do tabeli users dodaj kolumne e-mail'''
# mycursor.execute("Alter table users add column e_mail varchar(100)not null")

'''wprowadz dane tabel z list - user-data, user-scores'''
q3 = "INSERT INTO users (name,password,e_mail) values (%s, %s, %s)"
q4 = "INSERT INTO scores (userId, game1, game2) values (%s, %s, %s)"

# for i, user in enumerate(users_data):
#     mycursor.execute(q3,user)
#     last_id= mycursor.lastrowid
#     mycursor.execute(q4,(last_id,) + user_scores[i])
# mydb.commit()

# mycursor.execute("select* from scores")
# for i in mycursor:
#     print(i)

# mycursor.execute("select* from users")
# for i in mycursor:
#     print(i)

