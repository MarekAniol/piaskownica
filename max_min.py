from lista_flag import stworz_liste_flag


def dlugosci_flag(lista_flag):
    sorted_flags = sorted(lista_flag, key=len)
    return sorted_flags[0], sorted_flags[-1]


url = 'https://zajecia-programowania-xd.pl/flagi'

lista_flag = stworz_liste_flag(url)
shortest, longest = dlugosci_flag(lista_flag)
print(shortest)
print(longest)