### policz samogloski i spolgloski

zdanie = input("podaj jakies zdanie: ")
samogloski = 0
spolgloski = 0

lista_samogl = "aeiouyąęó"

#zdanie in lista_samogldfgdgz

for litera in zdanie:
    if litera.isalpha():
        if litera in lista_samogl:
            samogloski+=1
        else:
            spolgloski+=1

print (samogloski, " samoglosek w zdaniu")
print()
print (spolgloski, "spolglosek w zdaniu")