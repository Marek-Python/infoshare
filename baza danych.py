#### 1.PODSTAWOWE ####
#Napisz program, który będzie bazą kontaktów, program ma pytać użytkownika, co chce zrobić, dając mu minimum te opcje: dodanie imienia, usunięcie imienia, sprawdzenie czy imię jest w bazie, sprawdzenie ilości imion w bazie oraz zakończenie programu. Jeśli czujesz się pewniej to postaraj się aby użytkownik mógł podać więcej szczegółów np. nazwisko, nr telefonu, adres itp.
#
#Program ten będziemy pomału rozbudowywać, w kolejnych tygodniach
#
#Oczywiście piszemy już „Czysty kod” stosując się do konwencji Python’owych: piszemy docstringi, właściwe i znaczące nazwy zmiennych oraz funkcji. I jeśli damy radę to możemy postarać się stworzyć moduły z oddzielnymi funkcjonalnościami.




imie = [input ("Podaj imię: ")]
telefon = [input("Podaj numer telefonu: ")]

szukane_imie = input("Podaj imię, którego obecność w liście chcesz sprawdzić")


for szukane_imie in imie:
    if szukane_imie in imie == True:
        print ("To imię jest w zbiorze")
    else:
        print("Tego imienia nie ma w zbiorze")

usuwane_imie = input("Podaj imię, które chcesz usunąć z listy")

for usuwane_imie in imie:
    if usuwane_imie in imie == False:
        imie.remove(usuwane_imie)
        print ("imię zostało usunięte")
    else:
        print("Tego imienia nie ma w zbiorze")



print ("Ilośc imion w bazie to ", len(imie))

input("Aby zakończyć wciśnij enter")

if input=='':
    exit

