n = int(input("digite o valor de n: "))

soma = 0
operacoes = 0

for i in range(1, n + 1):
    soma += i
    operacoes += 1 

formula = n * (n + 1) // 2

print(f"""soma calculada: {soma})
numero de operações basicas: {operacoes}
soma pela formula matematica: {formula}""")