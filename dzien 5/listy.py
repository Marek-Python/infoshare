### do listy square chce dopisać 20 kwadratow
ile_liczb=20
squares=[]

for liczba in range(1,ile_liczb+1):
    squares.append(liczba**2)

print(squares)

### do listy square chce dopisać 20 kwadratow
#33ile_liczb=20#
#ubes=[]
#
#for liczba in range(1,ile_liczb+1):
 #   cubes.append(liczba**3)
#
#print(cubes)
#
#cubes = [ x ** 3 for x in range(1, ile_liczb +1)]
#
#print(cubes)
kolko_i_krzyzyk=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for podlista in kolko_i_krzyzyk:
    for element in podlista:
        print(element, end=" ")
    print()

lista=[[x, y] for x in range (5) for y in range (3)]
