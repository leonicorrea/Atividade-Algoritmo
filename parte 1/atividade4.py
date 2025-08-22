
numeros = input("digite os numeros com espaçamentos: ")

lista = [float(num) for num in numeros.split()]

media = sum(lista) / len(lista) if lista else 0

print(media)