import requests
import sys


def get_www_text(www):
    raw_info = requests.get(www)
    text = raw_info.text
    return text


def stworz_liste_flag(www: str) -> list:
    '''Zamienia text ze strony na listę flag'''
    text_www = get_www_text(www)
    list_links = text_www.split("</p>")
    links = []
    # Iteruje po wszystkich fragmentach tekstu HTML i do daję do listy tylko
    # te które mają url
    for linia in list_links:
        
        link = linia.replace("<p>", "")
        link = link.replace("- ", "")
        link = link.strip()
        if " " in link or "<" in link or "." not in link:
             continue
        if link.endswith("."):
            link = link[0:-1]
        if link not in links:
            links.append(link)
    return links


if __name__ == "__main__":
    argument = sys.argv[1] # dzięki temu można podać url w konsoli po wywołaniu pliku lista_flag.py
    lista_flag = stworz_liste_flag(argument)
    #print(lista_flag)
    # seen = set()
    # dupes = []

    # for f in lista_flag:
    #     if f in seen:
    #         dupes.append(f)
    #     else:
    #         seen.add(f)

    # print(len(lista_flag))
    # print(dupes)
    
