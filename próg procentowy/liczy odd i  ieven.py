### suma parzystych i nieparzystych w zakresie

zakres=range(1, 101)
print(zakres)
parzyste=0
nieparzyste=0

for liczba in zakres:
    if liczba%2 == 0:
        parzyste += 1
    else:
        nieparzyste += 1
print("parzyste: {} nieparzyste {}".format(parzyste,nieparzyste))