# ( DODATKOWE - Dla chętnych )
# Napisz program który wypisze dla podanej liczby (z zakresu od 1 do 100):
#   Dla wielokrotności 3-ki wypisz “Fizz”
#   Dla wielokrotności 5-tki “Buzz”.
#   Dla liczb które są wielokrotnością 3 i 5 napisz “FizzBuzz“
#   A jeśli liczba nie dzieli się ani przez 3 a ni przez 5, wypisz po prostu tą liczbę

liczba=(int)(input("podaj liczbę 1-100"))
if liczba%3==0 and liczba%5!=0:
    print ("Fizz")
if liczba%5==0 and liczba%3!=0:
    print ("Buzz")
if liczba%3==0 and liczba%5==0:
    print ("FizzBuzz")
elif liczba%3!=0 and liczba%5!=0:
    print (liczba)