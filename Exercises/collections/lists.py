bands = ["Metallica", "Rammstein", "Avenged Sevenfold", "Slipknot", "Rammstein", "System of a Down"]

print(bands[0]) #Retorna 1 índice
print(bands[-1]) #Retorna 1 índice de trás pra frente
print(bands[2:]) #Retorna a portir do segundo índice
print(bands[2:4]) #Retorna a portir do segundo índice até o quarto, excluindo o quarto índice
print(bands)
bands[3] = "Sabaton" # Substitui o valor de um índice
print(bands)

bands.extend(["Nirvana", "PowerWolf"]) #Adiciona vários itens a lista de uma vez
print(bands)

bands.append("Megadeth") #Adiciona apenas um item a lista
print(bands)

bands.insert(2, "Linkin Park") #Insere um valor no índice selecionado
print(bands)

bands.pop() #Remove o último índice
print(bands)

bands.remove("Linkin Park") #Remove o valor descrito dentro dos parenteses
print(bands)

# bands.clear() #Limpa a lista por completo
# print(bands)

print(bands.index("Rammstein")) # Retorna o número do índice com base no valor inserido
print(bands.count("Rammstein")) # Retorna a quantidade de vezes que o valor aparece na lista


list_numb = [2,6,4,3,1,7,9,5,8]
print(list_numb)

list_numb.sort() #Ordena a lista de inteiros em ordem crescente / funciona também com dados do tipo string, ordenando a lista em ordem alfabetica
print(list_numb)

list_numb.reverse() #Inverte a lista de trás para frente 
print(list_numb)

bands2 = bands.copy() #Salva uma cópia da lista numa variavel
bands.remove("Metallica") #Remove um valor da lista
print(bands) #Lista com um valor removido
print(bands2) #Cópia da lista original