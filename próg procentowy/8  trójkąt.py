# 8. podane 3 boki trojkata, okresl
#     - czy uda sie narysowac trojkata
#       * dl. jednego boku musi byc < dlugosc sumy dwoch pozostalych
#     - czy jest to tr. roznoboczny, rownoramienny czy rownoboczny

a=int(input("podaj bok a"))
b=int(input("podaj bok b"))
c=int(input("podaj bok c"))

if a < b+c and b < a+c and c <a+b:
    print ("to faktycznie jest trójkąt")
else:
    print ("to nie jest trójkąt")

#jak w tym miejscu zakończyć?


if a==b and b==c and c==a:
    print (" , co więcej jest to trójkąt równoboczny")

elif a!=b and  b!=c and c!=a:
    print (" i jest to trójkąt różnoboczny")

else:
    print (" równoramienny")



