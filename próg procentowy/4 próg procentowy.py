# 4. oblicz ocenę na podstawie progu procentowego
#

procent=int(input("podaj procent punktów"))
if procent <=70:
    print ("siadaj dwója")
if procent>70 and procent <=80:
    print ("dostateczny")
if procent>80 and procent <=90:
    print ("ocena dobra")
if procent>90:
    print ("ocena bardzo dobra")