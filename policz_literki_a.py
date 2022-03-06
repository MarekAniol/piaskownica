from lista_flag import stworz_liste_flag
import timeit


def count_letter_in_list(lst: list, letter: str) -> int:
    count_letter = str(lst).count(letter)
    return count_letter

url = "https://zajecia-programowania-xd.pl/flagi"
lista_f = stworz_liste_flag(url)
result = count_letter_in_list(lista_f, "a")
print(f"We flagach jest łącznie {result} liter 'a'.")

