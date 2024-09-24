
import mysql.connector
'''# połacz się z baza danych qatesting, i utwórz swójłacznik do komunikowania sie i wykonywania polecen na bazie danych  '''

mydb = mysql.connector.connect(host='localhost', password='1234password', user='root', database='qatesting')
mycursor = mydb.cursor()

print("................................................ex1 ")
'''tworze polecenie w dodzielnej zmiennej'''
#utwórz polecenie zeby adres emial Pani Ani zmieniony został na 'nowak@gmail.com'


print('')
print(".................................................ex2")
# wysietl wszytkich poza tymi co maja na imie Anna albo JAn


print('')
print(".............................................ex.3...... ")
# wysietl wszystkich o imionach Anna i Jan



print('')
print('.....................ex4..')
'''wysietli 5 pierwszych wpisow'''



print('')
print('.....................ex5..')
'''wysietli 5 ale zprzedzału ktory podam od 2-go wpisu'''


print('.....................ex6.')
#uporzadkuj imiona alfabetycznie od a-z



print('.....................z-a.')

#uporzadkuj imiona alfabetycznie od z-a


'''usun baze danych qatesting (jesli nie ma dalszych cwiczen)'''

