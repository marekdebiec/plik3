def wspolna(sek1, sek2):
    wynik =  []
    for x in sek1:
        if x in sek2:
            wynik.append(x)
    return wynik