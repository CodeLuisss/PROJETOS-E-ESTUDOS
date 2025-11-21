# UM PROGRAMA PARA CALCULAR A MÉDIA DE NOTAS DE UM ALUNO E DIZER SE FOI APROVADO OU NÃO

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
nota3 = float(input('Digite sua terceira nota: '))

media = (nota1 + nota2 + nota3) / 3


if media >= 7:
    print(f'Parabéns! Você foi aprovado com a média {media}!')
elif media == 6:
    print(f'A sua média é {media}, você foi para recuperação!')
else:
    print('REPROVADO!')
