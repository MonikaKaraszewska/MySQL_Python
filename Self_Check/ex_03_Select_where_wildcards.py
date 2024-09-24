import mysql.connector

'''# połacz się z baza danych qatesting, i utwórz swójłacznik do komunikowania sie i wykonywania polecen na bazie danych  '''

mydb = mysql.connector.connect(host='localhost', password='1234password', user='root', database='qatesting')
mycursor = mydb.cursor()

print('.................ex1.....')
'''wyswietl cała tablice testerzy'''


print('....................ex.2')
'''wyswietl tylko imiona z tablicy testerzy'''


print('....................................ex.3')
'''tworze polecenie w dodzielnej zmiennej, i wyszukaj tylko sosoby o imieniu Anna'''


print('')
print("....................exercise4...................")
'''co oznacza %'''
# wyswietl imiona które zaczynaja sie na 'an'


# wyswietl nazwiska które koncza sie na 'ski'
print("ski...")



# wyswietl nazwiska które maja w sobie 'ow'




'''usun baze danych qatesting (jesli nie ma dalszych cwiczen)'''
