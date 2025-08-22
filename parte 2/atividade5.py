print('CPF')

cpf = input("digite um cpf: ")

if len(cpf) == 11 and cpf.isdigit():
    print("CPF valido")
else:
    print("CPF invalido")
