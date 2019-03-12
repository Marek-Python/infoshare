# 5. znajdz liczbe stringow dl. min. 2, ktore zaczynaja sie i koncza na te same znaki
# ['abc', 'xyz', 'aba', '1221'] - odp = 2

lista=['abc', 'xyz', 'aba', '1221']

for element in lista:
    if  len(element)>=2 and element[0] == element[-1]:
        print(element)


# ten if moim zdaniem ma zrobi robotę, bo sprawdza czy oba warunki są spełnione
# ale po prostu nie wiem co napisać żeby pokazał te wyrazy
# jakieś print string if???



