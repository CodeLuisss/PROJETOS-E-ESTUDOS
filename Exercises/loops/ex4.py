# Some todos os números digitados pelo usuário até ele digitar 0.

n = int(input('Digite um número: '))

soma = 0

while n != 0:
    soma = soma + n
    n = int(input('Digite outro número: '))

print(soma)
