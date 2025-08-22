print('Faca login')
print('senha123')

sen = "senha123"
tent = 3

for i in range(tent):
    n = input('digite a senha: ')
    
    if n == sen:
        print("Seja bem-vindo")
        break
    else:
        print("senha incorreta")
else:
    print("acesso bloqueado")