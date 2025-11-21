# PROGRAMA PARA RECEBER 3 LADOS DE UM TRIANGULO E DIZER SE ELE É VÁLIDO

x = int(input('Digite o primeiro lado: '))
y = int(input('Digite o segundo lado: '))
z = int(input('Digite o terceiro lado: '))


soma1 = x + y
soma2 = x + z
soma3 = y + z


if soma1 > z and soma2 > y and soma3 > x:
    print('O triangulo é válido')
else:
    print('Triangulo inválido!')
