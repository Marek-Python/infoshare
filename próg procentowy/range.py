zakres= range (3,10)
for i in zakres:
    print(i)

nazwisko = "Strzelecki"
for litera in nazwisko[::2]:
    print(litera.upper())

litery = list(nazwisko)
print(litery)

moja_lista=[1,2,3,4,5,6,7,8,9]
print(moja_lista)
for cyfra in moja_lista:
    print(cyfra)

lista_liter=['s','t','r','z','e','l','e','c','k','i']
string_z_listy="".join(lista_liter)
print(string_z_listy)
string_z_listy="_".join(lista_liter)
print(string_z_listy)
string_z_listy="*".join(lista_liter)
print(string_z_listy)

#lista zakupów  = [1, "napis", "L",]
lista_zakupow  = ["jajko", "długopis", "kura"]
#opcja 1: for

for rzecz_do_kupienia in lista_zakupow:
    print(rzecz_do_kupienia)

#opcja 2

co_kupic = ", ".join(lista_zakupow)
print("chce kupić {}".format(co_kupic))


###

magic="abracadabra"
for i in range(len(magic)):
    print(i, magic[i])

####
zakres=range(10)
lista_z_zakresu = list(zakres)
print(lista_z_zakresu)

for i in zakres:
    print(i, end=", ")
print()
for i in lista_z_zakresu:
    print(i, end=", ")


