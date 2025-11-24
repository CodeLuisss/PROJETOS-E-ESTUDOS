# PROGRAMA PARA VERIFICAR SE O NUMERO INSERIDO ESTÁ ENTRE 10 E 50

num = int(input('Digite um número entre 10 e 50: '))

verificador = 10 <= num <= 50


if verificador:
    print(f'Legal! Seu número é {num}')
else:
    print('Digite um número entre os números solicitados!')
