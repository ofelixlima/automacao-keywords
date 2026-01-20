import requests
from time import sleep
print("AUTOMAÇÃO DE PESQUISAS")
keyword = str(input("Digite sua palavra-chave: ")).strip().lower()
opcoes = [{"nome": "Google", "endpoint": f"http://google.com/complete/search?client=chrome&q={keyword}"}, {"nome": "YouTube", "endpoint": f"https://suggestqueries.google.com/complete/search?client=chrome&ds=yt&q={keyword}"}]
escolha = int(input("Onde você quer pesquisar?\n[0] Google\n[1] YouTube\nDigite um número: "))
print(f"Pesquisando {keyword.upper()} no {opcoes[escolha]["nome"].upper()}...")
alfabeto = {"letras": " abcdefghijklmnopqrstuvwxyz"}
letras = [l for l in alfabeto['letras']]
for c in range(len(letras)):
    if letras[c] == " ":
        api = requests.get(opcoes[escolha]["endpoint"])
    else:
        api = requests.get(f"{opcoes[escolha]["endpoint"]}%{letras[c]}")
    sugestoes = api.json()
    if letras[c] == " ":
        print(f"\nSugestões EM ALTA sobre {keyword.upper()}:")
    else:
        print(f"\nSugestões para {keyword.upper()} {letras[c].upper()}:")
    for p in range(len(sugestoes[1])):
        print(sugestoes[1][p])
    sleep(2)