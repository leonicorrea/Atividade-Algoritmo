print('Estatísticas de Notas')

n1 = int(input("quantos alunos? "))
notas = []

for i in range(n1):
    nota = float(input(f"digite a nota do aluno {i+1}: "))
    notas.append(nota)

def estatisticas(notas):
    media = sum(notas) / len(notas)
    maior = max(notas)
    menor = min(notas)
    
    acima_media = sum(1 for nota in notas if nota > media)
    percentual_acima = (acima_media / len(notas)) * 100
    
    return media, maior, menor, percentual_acima

media, maior, menor, percentual = estatisticas(notas)

print(f"\n estatisticas da turma:")
print(f"media: {media:.2f}")
print(f"maior nota: {maior}")
print(f"menor nota: {menor}")
print(f"percentual de alunos acima da media: {percentual:.2f}%")