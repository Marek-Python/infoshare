# 1. sprawdź czy jest wygrana w kółko i krzyżyk
#   input: string 9 znaków x, o, n
#   znaki oznaczają pozycje wierszami od gornego

input:"podaj x,o, sztuk 9"
    if "x" in [0:1:2]
        or "x" in [3:4:5]
        or "x" in [6:7:8]
        or "x" in [0:4:8]
        or "x" in [2:4:6]
            print "krzyżyk"
if "o" in [0: 1: 2]
or "o" in [3: 4:5]
or "o" in [6: 7:8]
or "o" in [0: 4:8]
                or "x" in [2: 4:6]
print
"kółko"