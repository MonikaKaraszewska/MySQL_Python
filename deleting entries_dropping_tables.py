import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', password='1234password',database='qatesting')
mycursor=mydb.cursor()

# usun daneososby i imieniu'anna

# delete = "Delete from testerzy where imie='Anna'"
# mycursor.execute(delete)
# mydb.commit()
#

# usun kolumne adres_email
# mycursor.execute('Alter table testerzy drop column adres_email')
# mydb.commit()

# dodaj od tableki testerzy kolumne age
# mycursor.execute("alter  table  testerzy add (age VARCHAR(200))")
# mydb.commit()

# dla osobu o id=1 wprowadz wiek=45
mycursor.execute("update testerzy set age=45 where id=1 ")
mydb.commit()

