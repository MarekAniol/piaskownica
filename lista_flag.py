import requests
import sys

x = [1,2,3]
for i in x:
    print(i)

def get_www_text(www):
    raw_info = requests.get(www)
    text = raw_info.text
    return text


def stworz_liste_flag(www: str) -> list:
    text_www = get_www_text(www)
    list_links = text_www.split("</p>")
    links = []
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
    argument = sys.argv[1]
    lista_flag = stworz_liste_flag(argument)
