from lista_flag import stworz_liste_flag


# Funkcja 1. Ile jest domen które mają '.pl' (nie ważne czy mają '.edu.pl')
def licz_flagi_pl(flagi):
    licznik_pl = len([f for f in flagi if ".pl" in f])
    for l in sorted([f for f in flagi if ".pl" in f]):
        print(l)
    return licznik_pl


url = "https://zajecia-programowania-xd.pl/flagi"
lista_f = stworz_liste_flag(url)
wynik = licz_flagi_pl(lista_f)
print(f"Domen kończących się na '.pl' jest {wynik}.")
