#EXEMPLO DE LAÇO INFINITO

while True:
    user = input('digite seu usuário: ')
    senha = input('digite a senha: ')

    if user == 'adm' and senha == '123':
        print('acesso liberado.')
        break
    else:
        print('usuário ou senha não conferem, digite novamente.')
        continue
