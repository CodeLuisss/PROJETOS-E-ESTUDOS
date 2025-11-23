# PROGRAMA PARA VERIFICAR SE A SENHA QUE O USUÁRIO DEU ENTRADA É A CORRETA

senha = int(input('Digite a senha correta: '))

senha_correta = 1234


if senha == senha_correta:
    print('Sua senha está correta!')
else:
    print('Senha incorreta!')
