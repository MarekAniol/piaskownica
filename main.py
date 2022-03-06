from functions import*
from lista_flag import stworz_liste_flag


url = "https://zajecia-programowania-xd.pl/flagi"


if __name__ == "__main__":
    
    lista_f = stworz_liste_flag(url)
    flagi_pl = licz_flagi_pl(lista_f)
    shortest, longest = dlugosci_flag(lista_f)
    flagi_com = licz_flagi_com(lista_f)
    result_letter = count_letter_in_list(lista_f, "a")

    print(f"Domen kończących się na '.pl' jest {flagi_pl}.")
    print(f"Najkrotsza i najdluższa: {shortest}, {longest}.")
    print(f"Domen, które mają samo '.com' jest {flagi_com}.")
    print(f"We flagach jest łącznie {result_letter} liter 'a'.")