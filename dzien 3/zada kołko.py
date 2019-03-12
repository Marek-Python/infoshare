# 1. sprawdź czy jest wygrana w kółko i krzyżyk
#   input: string 9 znaków x, o, n
#   znaki oznaczają pozycje wierszami od gornego

# 2. obliczanie roku przestępnego
# podzielny przez 4, nie podzielny przez 100 ale podzielny przez 400

# 3. czy liczba jest podzielna przez 3, 5, 7

# 4. oblicz ocenę na podstawie progu procentowego

procent=input (int)("podaj procent punktów")
if procent <=70:
    print ("siadaj dwója")
if procent>70 and procent <=80:
    print ("dostateczny")
if procent>80 and procent <=90:
    print ("ocena dobra")
if procent>90:
    print ("ocena bardzo dobra")


# 5. ruletka: otrzymawszy liczbę, sprawdź czy jest ona:
#   czerwona czy czarna*
#   wysoka czy niska (do 18, od 18)
#   parzysta czy nieparzysta

numer=int(input("podaj liczbę na stole"))
if numer(range(10))%2==0 or numer(range (11,17))%2!=0\
        or numer(range(20,28)%2==0 or numer(range(29,35))%2!=0):
            print ("czarne")
elif print ("czerwone"):

    if numer==0:
        print ("wygrywa kasyno")
if numer%2==0:
    print ("parzyste")
if numer%2!=0:
    print ("nieparzyste")
if numer>=1 and numer<=18:
    print ("niskie")
if numer>18 and numer<=36:
    print ("wysokie")
if numer(range(10))%2==0 or numer(range (11,17))%2!=0\
        or numer(range(20,28)%2==0 or numer(range(29,35))%2!=0):
            print ("czarne")
elif print ("czerwone"):




# 6. blackjack - na inpucie wejście 2 karty
#   wartości: 2-9, J Q K = 10, A = 1 lub 11
#   określ ruch jaki powinien być wykonany:
#   jeszcze jedna karta, stop,



# 7. po podaniu nazwy miesiaca, program napisze ilosc dni w miesiacu

# 8. podane 3 boki trojkata, okresl
#     - czy uda sie narysowac trojkata
#       * dl. jednego boku musi byc < dlugosc sumy dwoch pozostalych
#     - czy jest to tr. roznoboczny, rownoramienny czy rownoboczny

# 9. inupt - miesiąc oraz dzien,
#   okreslic pore roku

miesiac=int(input("podaj numer miesiaca"))
dzien=int(input("podaj dzien miesiaca"))

if miesiac==1 or miesiac==2 or (miesiac==12 and dzien>=21) or (miesiac==3 and dzien <20):
    print ("zima")

if miesiac == 4 or miesiac == 5 or (miesiac == 3 and dzien >= 21) or (miesiac == 6 and dzien < 20):
    print ("wiosna")

if miesiac==7 or miesiac==8 or (miesiac==6 and dzien>=21) or (miesiac==9 and dzien <20):
    print ("lato")

if miesiac==10 or miesiac==11 or (miesiac==9 and dzien>=21) or (miesiac==12 and dzien <20):
    print ("jesień")

# jak ograniczyć max liczbe dni

# 10. zamiana temperatury
#     wejscie: "35C" "100F"
#     wyjście "Temperatura w {typ} to {xxx} stopni"
#     C = (F - 32) * (5/9)
#     F = C * (9 / 5) + 32

# 10. zamiana temperatury
#     wejscie: "35C" "100F"
#     wyjście "Temperatura w {typ} to {xxx} stopni"
#     C = (F - 32) * (5/9)
#     F = C * (9 / 5) + 32

c=35
f=100

c_na_f=(f-32)*(5/9)
f_na_c=c*(9/5)+32

print ("Temperatura w ") and print (c) and print
       print
print ("Temperatura w ") (f) ("to "(f_na_c)) ("stopni")

# nie wiem jak to wyświetlić

# 10. zamiana temperatury
#     wejscie: "35C" "100F"
#     wyjście "Temperatura w {typ} to {xxx} stopni"
#     C = (F - 32) * (5/9)
#     F = C * (9 / 5) + 32

c=35
f=100

c_na_f=(f-32)*(5/9)
f_na_c=c*(9/5)+32

print (c_na_f)
print (f_na_c)

print ("Temperatura w ") and print (c) and print
       print
print ("Temperatura w ") (f) ("to "(f_na_c)) ("stopni")