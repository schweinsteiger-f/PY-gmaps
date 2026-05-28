# Python Google-Maps V.0.0.1
import webbrowser
import urllib
from urllib import parse
import colorama
from colorama import Fore, Back, Style
import time
colorama.init()
print(Fore.LIGHTCYAN_EX + "Bem-vindo ao Gmaps em python! Repositorio do projeto: https://github.com/schweinsteiger-f/PY-Gmaps")
print("Iniciando....")
time.sleep(2)
localidade_codificada = urllib.parse.quote_plus(input("Digite aqui a localidade que você gostaria de pesquisar: "))
link = f"https://www.google.com/maps/search/?api=1&query={localidade_codificada}"
print(f"aqui esta o link: {link}")
quest = input("Quer ir ate o site? Sim(1) Não(2)")
if quest == "1":
    print(Fore.RED + "Adeus!")
    time.sleep(1)
    webbrowser.open(link)
else:
    None
    print(Fore.RED + "Adeus!")
