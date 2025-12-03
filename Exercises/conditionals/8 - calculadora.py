print('1. Adição')
print('2. Subtração')
print('3. Divisão')
print('4. Multiplicação')

operacao = int(input('Selecione qual operação quer fazer: '))


x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))


if operacao == 1:
    print(f'O resultado da soma é {x + y}')

elif operacao == 2:
    print(f'O resultado da subtração é {x - y}')

elif operacao == 3:
    if y == 0:
        print('Não é possivel dividir por Zero!')
    else:
        print(f'O resultado da divisao é {x / y}')

elif operacao == 4:
    print(f'O resultado da multiplicação é {x * y}')

else:
    print('Selecione uma operação válida!')
