# Conte quantos números o usuário digitou até digitar 0.

digitos = 0

n = int(input('Digite um número: '))

while n != 0:
    digitos += 1
    n = int(input('Digite mais um número: '))

print(digitos)
