###   *
###  ***
### *****
### podana liczba to liczba poziomów


wysokosc = int(input("podaj wysokosc"))
#2n-1
napis_poczatek = "*" * (2 * wysokosc -1)
spacje=""
while len(napis_poczatek)>1:

    print("{}{}".format(spacje, napis_poczatek))
    print(napis_poczatek)
    if len(napis_poczatek)>2:
        napis_poczatek=napis_poczatek[:-2]
    spacje= spacje + " "