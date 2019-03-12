lista = [1,2,3,4,5,4,3,2,1]
lista_bez_duplikatow=[]

for element in lista:
    if element not in lista_bez_duplikatow:
        lista_bez_duplikatow.append(element)
print(lista_bez_duplikatow)

zbior=set(lista)
zbior=list(set(lista))
print (zbior)
