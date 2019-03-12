# 8. program sprawdza czy dwie listy maja co najmniej jeden wspolny element,
# jesli tak wypisuje True

a = [10,20,30,20,10,50,60,40,80,50,40]
b = [3,4,5,6,6]

if bool(set(a)& set(b))==True:
    print("True")
else:
    print ("False")

