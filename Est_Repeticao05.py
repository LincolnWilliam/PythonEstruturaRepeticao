# Leia 3 notas e informe a média para o usuário
cont = 1
media = 0

while cont <= 3:
    nota = int(input('digite a nota: '))
    media += nota
    cont +=1
media = media/3
print (f'a media das notas é: {media}')
