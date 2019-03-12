ile_liczb=10

for n in range (2, ile_liczb):
    if n%2==0:
        print (n, "parzysta")
        continue
    print(n, "nieparzysta")