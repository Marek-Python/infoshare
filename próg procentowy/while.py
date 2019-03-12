x = True
while x:
    print (x)
    x=False
print ("już poza while")


password = input("podaj hasło")
while len(password) < 6:
    print ("hasło za krótkie")
    password = ("podaj nowe hasło")

print(f"twoje hasło to {password} a jego dlugosc to {len(password)}")
print("twoje hasło to {} a jego dlugosc to {}.format(password, {len(password)}")