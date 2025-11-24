temp = int(input('Digite a temperatura em °C: '))


if temp < 0:
    print('Congelante!')
elif temp <= 20:
    print('Frio!')
elif temp <= 30:
    print('Agradavel!')
else:
    print('Quente!')
