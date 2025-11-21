# PROGRAMA PARA VERIFICAR SE O NÚMERO É POSITIVO, NEGATIVO OU ZERO

x = int(input('Digite um número: '))


if x > 0:
    print('O número é positivo!')
elif x == 0:
    print(f'O número é {x}')
else:
    print('O número é negativo!')
