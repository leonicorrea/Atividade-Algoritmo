print('Busca Linear')


n1 = int(input('quantos nomes voce vai escrever ?: '))
nomes = []

for i in range(n1):
    nome = (input(f"digite os nome {i+1}: "))
    nomes.append(nome)

def busca(lista, nome):
    for i in range(len(lista)):
        if lista[i].lower() == nome.lower():
            return i
    return -1

nomeprocurado = input("digite um nome para buscar: ")

posicao = busca(nomes, nomeprocurado)

if posicao != -1:
    print(f"O nome '{nomeprocurado}' foi encontrado na posição {posicao}.")
else:
    print(f"O nome '{nomeprocurado}' nao foi encontrado na lista.")