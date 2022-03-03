from lista_flag import stworz_liste_flag
import timeit


# Funkcja 3. Ile jest literek 'a' we wszstkich domenach razem.
def count_letter_in_list(lst: list, letter: str) -> int:
    count_letter = str(lst).count(letter)
    return count_letter

def counts_character(links, character):
    counter = 0
    for link in links: 
        for char in link: 
            if char == 'a':    #  'a' in the string'
                counter += 1
            else:
                counter = counter
    return counter



url = "https://zajecia-programowania-xd.pl/flagi"
lista_f = stworz_liste_flag(url)
result = count_letter_in_list(lista_f, "a")
print(f"We flagach jest łącznie {result} liter 'a'.")

duration1 = timeit.repeat('count_letter_in_list(lista_f, "a")', number=1000000, globals=globals(), repeat=1)
print("Function (count_letter_in_list) duration is:", end=' ')
print(sum(duration1)/len(duration1))

duration2 = timeit.repeat('counts_character(lista_f, "a")', number=1000000, globals=globals(), repeat=1)
print("Function (counts_character) duration is:", end=' ')
print(sum(duration2)/len(duration2))
