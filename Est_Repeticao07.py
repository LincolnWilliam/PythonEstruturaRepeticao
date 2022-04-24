#EXIBIR UM NÚMERO SORTEADO
#caso fique com erro no random, importe o pacote -> import random

#JOGUINHO DO USUARIO ACERTAR O NUMERO SORTEADO ENTRE ( 1 e 10)
# Ler README.md
import random

sorteado = random.randrange(1,10)
print(sorteado)

while True:
    numero = int(input('Informe o número sorteado: '))

    if numero == sorteado:
        print('Parabéns você acertou !!')
        break
    elif numero > sorteado:
        print('palpite muito alto, diminua o número.')
    else:
        print('palpite muito baixo, aumente o número.')
