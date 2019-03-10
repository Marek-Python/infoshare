
# 6. program znajdujacy wartosci, ktre wystepuja tylko raz
lista_a = [10,20,30,20,10,50,60,40,80,50,40]
print(set([i for i in lista_a if lista_a.count(i)==1]))

