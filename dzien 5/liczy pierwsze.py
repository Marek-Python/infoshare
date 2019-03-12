#break, continue
ile_liczb=100
for n in range(2, ile_liczb):
    for x in range(2,n):
        if n % x == 0:
            print(f"{n} jest liczbą złożoną")
            break
    else:
        print(f"{n} jest liczbą pierwszą")
