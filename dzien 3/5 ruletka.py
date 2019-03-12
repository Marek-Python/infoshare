# 5. ruletka: otrzymawszy liczbę, sprawdź czy jest ona:
#   czerwona czy czarna*
#   wysoka czy niska (do 18, od 18)
#   parzysta czy nieparzysta

numer=(int)(input("podaj liczbę na stole"))

# sprawdziłem na https://pl.wikipedia.org/wiki/Ruletka_(gra) układ czerwone i czarne i chciałem to podać jako zakresy ale nie wyszło
if numer(range(1,10))%2==0 or numer(range(11,17))%2!=0 or numer(range(20,28)%2==0 or numer(range(29,35))%2!=0):
            print ("czarne")
else:
    print ("czerwone")
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
else:
    print("czerwone")