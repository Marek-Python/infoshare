# 9. input - miesiąc oraz dzien,
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


