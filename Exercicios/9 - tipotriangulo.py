# PROGRAMA PARA VERIFICAR O TIPO DE TRIANGULO DE ACORDO COM O TAMANHO DOS LADOS

x = int(input('Digite o primeiro lado: '))
y = int(input('Digite o segundo lado: '))
z = int(input('Digite o terceiro lado: '))


if x == y and x == z and y == z:
    print('O triangulo é Equilatero!')
elif x == y or x == z or y == z:
    print('O triangulo é Isóceles!')
elif x != y and x != z and y != z:
    print('O triangulo é Escaleno!')
