from lista_flag import stworz_liste_flag


def policz_domeny_len(linki):
    wynik = 0

    for l in linki:
        if len(l)> wynik:
            wynik = len(l)
            print(l)
    return wynik


url = "https://zajecia-programowania-xd.pl/flagi"
lista_f = stworz_liste_flag(url)
result = policz_domeny_len(lista_f)
print(result)
