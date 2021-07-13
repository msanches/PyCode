import os
os.system('cls||clear')
soma = 0
contador = 0
num = 1
resp=input("Quer fazer a média s/n?")

while resp=='s' and num!=0:
  num = int(input("\033[1;94mDigite um número inteiro ou zero para sair: \033[0;0ms"))
  soma = soma + num
  if num!=0:
    contador= contador + 1

media = soma/contador
print(f"A média é {media:.2f}")