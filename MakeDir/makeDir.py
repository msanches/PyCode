import os
while True:
    diretorio = input("Digite o nome do diretório: ")
    if diretorio == '':
        break
    try:
        os.makedirs(diretorio)
    except OSError:
        print("Não foi possível criar o diretório!")
