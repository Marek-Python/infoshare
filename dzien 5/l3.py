

# 3. program wydający resztę z podanych monet []
# (czyli teraz uzytkownik moze podac monety),
# wczytujemy dostępne monety z input'a dopóki nie dostaniemy znaku "Q"

#### bankomat, wydaje z kwoty jak najmniejszą liczbę monet (5, 2, 1, .5 ,.2, .1)

reszta=float(input("ile mam wydać reszty"))
dostepne_monety = [5, 2, 1, 0.5, 0.2, 0.1]
reszta_w_monetach=[]

while (reszta >= 0.1):
    for moneta in dostepne_monety:
        #jesli moneta ma mniejsza wartosc niz reszta, to mozemy dodac taką monetę do monet w reszcie
        if moneta <= reszta:
            #najpierw wydajemy monete
            reszta_w_monetach.append(moneta)
            #teraz liczymy ile zostalo pieniedzy do wydania
            reszta= reszta - moneta
            break

czy_reszta = input("czy moge byc winna grosika?")

if czy_reszta.lower()=="tak":
    reszta_w_monetach.append(0.1)
