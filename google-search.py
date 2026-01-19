import requests
from time import sleep
keyword = "google" #str(input("Digite sua palavra-chave: ")).strip().lower()
alfabeto = {"letras": " abcdefghijklmnopqrstuvwxyz"}
letras = [l for l in alfabeto['letras']]
for c in range(len(letras)):
    if letras[c] == " ":
        api = requests.get(f"http://google.com/complete/search?client=chrome&q={keyword}")
    else:
        api = requests.get(f"http://google.com/complete/search?client=chrome&q={keyword}%{letras[c]}")
    sugestoes = api.json()
    if letras[c] == " ":
        print(f"\nSugestões para {keyword.upper()}:")
    else:
        print(f"\nSugestões para {keyword.upper()} {letras[c].upper()}:")
    for p in range(len(sugestoes[1])):
        print(sugestoes[1][p])
    sleep(2)