# 2. obliczanie roku przestępnego
# podzielny przez 4, nie podzielny przez 100 ale podzielny przez 400

rok=input ("podaj rok")
rok=int(rok)
if rok%400==0:
    print ("rok przestępny")
elif rok%4==0 and rok%100!=0:
    print ("rok przestępny")
else:
    print ("rok nieprzestępny")