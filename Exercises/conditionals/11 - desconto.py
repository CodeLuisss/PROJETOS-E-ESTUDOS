preco = float(input('Insira o valor do produto: '))

print('1. Sim')
print('2. Não')
selecione_cupom = int(input('Você tem cupom? '))


if selecione_cupom == 1:
    preco = preco - (preco * 0.10)
    print(f'O valor total da sua compra com o cupom é de R${preco:.2f}')
elif selecione_cupom == 2:
    print(f'O valor total da sua compra é de R${preco:.2f}')
else:
    print('Digite uma opção válida!')
