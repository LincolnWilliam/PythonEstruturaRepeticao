# Leia 10 números e informe quantos são pares e quantos são ímpares
cont = 1
qtdePar = 0
qtdeImpar = 0

while cont <= 10:
    numero = int(input('informe um número: '))
    if numero % 2 == 0:
        qtdePar = qtdePar + 1

    else:
        qtdeImpar = qtdeImpar + 1

    cont +=1
print(f'a quantidade de números pares é: {qtdePar}')
print(f'a quantidade de números impares é: {qtdeImpar}')

