from lista_flag import stworz_liste_flag


# Funkcja 2. Ile jest domen które mają samo '.com'
def licz_flagi_com(flagi):
    result = len([f for f in flagi if f.endswith(".com")])
    return wynik


url = "https://zajecia-programowania-xd.pl/flagi"
lista_f = stworz_liste_flag(url)
wynik = licz_flagi_com(lista_f)
print(f"Domen, które mają samo '.com' jest {wynik}.")
