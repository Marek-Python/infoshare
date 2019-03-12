# 11. oblicz częstość elementów w liście (ile razy)
# jedna wersja zwykla pętle, ify itd
# druga - moze jest jakis modul gotowy???
my_list = [10,10,20,10,10,20,10,20,20,20,40,50,40,10,30,50,50,30]



from collections import Counter
my_list = [10,10,20,10,10,20,10,20,20,20,40,50,40,10,30,50,50,30]
count_my_list = Counter(my_list)
output_list= []

for i in count_my_list:
    output_list.append([i,count_my_list[i]])
print(output_list)