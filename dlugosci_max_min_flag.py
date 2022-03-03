from lista_flag import stworz_liste_flag


def get_min_max_domain(lst):
    domains_with_lenght = [(len(d), d) for d in sorted(lst, key=len)]
    return domains_with_lenght[0], domains_with_lenght[-1]


url = 'https://zajecia-programowania-xd.pl/flagi'

lst = stworz_liste_flag(url)
shortest, longest = get_min_max_domain(lst)
print(f"Shortest domain: {shortest}")
print(f"Longest domain: {longest}")
