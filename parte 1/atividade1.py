print('Escreva dois numeros')

n1 = int(input('escreva o primeiro numero: '))
n2 = int(input('escreva o segundo numero: '))

def calculo():
    if n1 < n2:
        print(f'{n2} e o maior numero')
    
    elif n2 < n1:
        print(f'{n1} e o maior numero')
    
    else:
        print('os dois sao iguais')

calculo()

