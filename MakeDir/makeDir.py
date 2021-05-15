import os
while True:
    nome = input("Digite o nome do aluno: ")
    if nome == '':
        break
    try:
        os.makedirs(nome)
    except OSError:
        print("Não foi possível criar o diretório!")

#dir = 'temp2'       
#os.makedirs(dir)
# ou 
#os.mkdir(dir)