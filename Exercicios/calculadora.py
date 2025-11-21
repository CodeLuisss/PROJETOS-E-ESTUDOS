# CALCULADORA SIMPLES

# AQUI EU VOU PEDIR PARA O USUÁRIO SELECIONAR QUAL OPERAÇÃO MATEMÁTICA ELE QUER FAZER

operacao = int(input('Selecione qual operação quer fazer: '))
print('1. Adição')
print('2. Subtração')
print('3. Divisão')
print('4. Multiplicação')


# AQUI O USUÁRIO VAI DAR ENTRADA EM DOIS NÚMEROS INTEIROS

x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))


# AQUI SERÁ ARMAZENADAS AS OPERAÇÕES DENTRO DAS VARIÁVEIS

soma = x + y
sub = x - y
divisao = x / y
multi = x * y


# AQUI SERÁ MOSTRADO PARA O USUÁRIO O RESULTADO DA OPERAÇÃO

if operacao == 1:
    print(f'O resultado da soma é {soma}')
elif operacao == 2:
    print(f'O resultado da subtração é {sub}')
elif operacao == 3:
    print(f'O resultado da divisao é {divisao}')
elif operacao == 4:
    print(f'O resultado da multiplicação é {multi}')
else:
    print('Selecione uma operação válida!')
