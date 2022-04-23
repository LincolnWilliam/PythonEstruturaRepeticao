# Faça a tabuada (multiplicação) de um número informado pelo usuário
cont = 1
numero = int(input('informe número da tabuada que deseja: '))
while cont <=10:
    print(f'{numero} X {cont} = {numero * cont}')
    cont += 1