# 10. zamiana temperatury
#     wejscie: "35C" "100F"
#     wyjście "Temperatura w {typ} to {xxx} stopni"
#     C = (F - 32) * (5/9)
#     F = C * (9 / 5) + 32

c=35
f=100

c_na_f=(f-32)*(5/9)
f_na_c=c*(9/5)+32

print ("Temperatura w ") and print (c) and print
       print
print ("Temperatura w ") (f) ("to "(f_na_c)) ("stopni")