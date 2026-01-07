# Crie uma lista com nomes e verifique se um nome específico existe na lista.

lista = ["Carol", "Marcia", "Marcio", "Marcus", "Ane", "Angelina", "Aninha", "Dede"]

name = input('Digite um nome para saber se está na lista: ')

if name in lista:
    print('O nome está na lista!')
else:
    print('O nome não está na lista!')
