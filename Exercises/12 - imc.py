peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura ** 2)


if imc < 18.5:
    print('Você está abaixo do seu peso normal!')
elif imc <= 24.9:
    print('Seu peso está normal!')
elif imc <= 29.9:
    print('Alerta de excesso de peso!')
elif imc <= 34.9:
    print('Obesidade tipo I')
elif imc <= 39.9:
    print('Obesidade grau II')
elif imc >= 40.0:
    print('Obesidade grau III')
