def Bhaskara(a, b , c):
    delta = (b ** 2) - (4 * a * c)
    if delta >=0:    
        x1 = (-b + delta ** (1 / 2)) / (2 * a)
        x2 = (-b - delta ** (1 / 2)) / (2 * a)
        print('\nValor de x1: {0}'.format(x1))
        print('Valor de x2: {0}'.format(x2))
    else:
        print('Não há raízes reais!')

while True:
    print('Calculando as raízes de uma equação de 2º grau\n')
    
    a = float(input('Digite um valor para A: '))
    b = float(input('Digite um valor para B: '))
    c = float(input('Digite um valor para C: '))
    if a==0:
        print('Não é equação do 2º grau!!')
    else:
        Bhaskara(a, b, c)

    continua = input('\nDeseja sair? Digite q ou Enter para um novo cálculo: \n')
    if (continua == 'q'):
        break