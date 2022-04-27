# Quantidade de par e impar
i = 1
par = 0
impar = 0
for i in range(1, 51):
    if i % 2 == 0:
        par += 1
    else:
        impar += 1
    print(i)

print(f'os {i} números possuem: {par} números pares e {impar} números impares')