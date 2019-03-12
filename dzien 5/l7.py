# 7. program usuwajacy zduplikowane wartosci w liscie (w miejscu! - tzn bez drugiej listy)
#niestety moja metoda nie działa

lista_b = [10,20,30,20,10,50,60,40,80,50,40]
lista_b.pop([i for i in lista_b if lista_b.count(i)!=1])

print (lista_b)
