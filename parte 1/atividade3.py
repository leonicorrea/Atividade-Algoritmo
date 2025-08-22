print('DESCUBRA O NUMERO PRIMO')

n = int(input('escreva um numero: '))

def primo():
    if n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1)):
        print(f"{n} e um numero primo")

    else:
        print(f'{n} nao e primo')

primo()
      
