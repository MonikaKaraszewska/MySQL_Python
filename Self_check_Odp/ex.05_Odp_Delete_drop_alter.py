import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', password='1234password',database='qatesting')
mycursor=mydb.cursor()

print('....ex1....')
# usun dane ososby i imieniu'anna

# delete = "Delete from testerzy where imie='Anna'"
# mycursor.execute(delete)
# mydb.commit()
#
print('....ex2....')

# usun kolumne adres_email
# mycursor.execute('Alter table testerzy drop column adres_email')
# mydb.commit()

print('....ex3....')

# dodaj od tableki testerzy kolumne age
# mycursor.execute("alter  table  testerzy add (age VARCHAR(200))")
# mydb.commit()

print('....ex4....')

# dla osobu o id=1 wprowadz wiek=45
mycursor.execute("update testerzy set age=45 where id=1 ")
mydb.commit()

