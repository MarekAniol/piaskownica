def dlugosci_flag(lista_flag):
    maxlen = max(lista_flag, key=len)
    minlen = min(lista_flag, key=len)
    return maxlen, minlen


def licz_flagi_pl(flagi):
    licznik_pl = len([f for f in flagi if ".pl" in f])
    return licznik_pl


def licz_flagi_com(flagi):
    result = len([f for f in flagi if f.endswith(".com")])
    return result


def count_letter_in_list(lst: list, letter: str) -> int:
    count_letter = str(lst).count(letter)
    return count_letter

from lista_flag import stworz_liste_flag

if __name__ == "__main__":
    
    url = "https://zajecia-programowania-xd.pl/flagi"
    lista_f = stworz_liste_flag(url)
    print(dlugosci_flag(lista_f))