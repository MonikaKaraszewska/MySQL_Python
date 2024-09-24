import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', password='1234password',database='qatesting')
mycursor=mydb.cursor()

print('............ex1....')
'''# usun dane ososby i imieniu'anna'''



print('...................ex2....')
'''# usun kolumne adres_email'''

print('............ex3....')
'''# dodaj od tableki testerzy kolumne age'''

print('................ex4....')
'''# dla osobu o id=1 wprowadz wiek=45'''


'''usun baze danych qatesting (jesli nie ma dalszych cwiczen)'''
