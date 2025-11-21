# PROGRAMA PARA CLASSIFICAR AS IDADES ENTRE MENOR, ADULTO OU IDOSO

idade = int(input('Digite sua idade: '))


if idade < 18:
    print('Você é menor de idade!')
elif idade >= 18 and idade <= 59:
    print('Você é Adulto!')
else:
    print('Você é idoso!')
