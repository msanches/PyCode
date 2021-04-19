#pip install pyshorteners
import pyshorteners

url = input("Entre com a url: ")

#carrega a lib
s = pyshorteners.Shortener()

#gera a url encurtada
shortURL = s.tinyurl.short(url)

#mostra a url encurtada
print(f"URL encurtada: {shortURL}")