liczba=int(input("podaj liczbę"))
if liczba%3==0 and liczba%5==0 and liczba%7==0:
    print ("podzielna przez 3, 5 i 7")
elif liczba%3==0 and liczba%5==0:
    print ("podzielna przez 3 i 5")
elif liczba%5==0 and liczba%7==0:
    print ("podzielna przez 5 i 7")
elif liczba%3==0 and liczba%7==0:
    print ("podzielna przez 3 i 7")
