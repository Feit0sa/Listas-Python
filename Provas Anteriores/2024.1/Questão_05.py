RelacaoAlunos = []

for i in range(7):
    linha = []
    linha.append(input(f"Digite o nome do {i+1}° aluno(a): "))
    linha.append(float(input(f"Digite a nota do {i+1}° aluno(a): ")))
    linha.append(input(f"Digite o curso do {i+1}° aluno(a): "))
    linha.append(input(f"Digite a situação do {i+1}° aluno(a): "))
    print("==============================")
    RelacaoAlunos.append(linha)

print()
print("============Matriz============")
for i in range(7):
    print(RelacaoAlunos[i])
print()
print("==========Média geral=========")
MediaGeral = 0
for i in range(7):
    MediaGeral += RelacaoAlunos[i][1]/7
print(MediaGeral)
print()
print("=======Relação de Cursos======")
AlunosComp, AlunosInfo, AlunosRede = 0, 0, 0
for i in range(7):
    if RelacaoAlunos[i][2] == "Computação":
        AlunosComp += 1
    elif RelacaoAlunos[i][2] == "Informática":
        AlunosInfo += 1
    else:
        AlunosRede += 1
print(f"Quantidade de Alunos de Computação: {AlunosComp}")
print(f"Quantidade de Alunos de Informática: {AlunosInfo}")
print(f"Quantidade de Alunos de Redes: {AlunosRede}")
print()
print("=======Relação Aprovados=======")
PercentualAprovados, PercentualReprovados = 0, 0
for i in range(7):
    if RelacaoAlunos[i][3] == "Aprovado":
        PercentualAprovados += (1/7)*100
    else:
        PercentualReprovados += (1/7)*100
print(f"Percentual de Alunos Aprovados: {PercentualAprovados}%")
print(f"Percentual de Alunos Reprovados: {PercentualReprovados}%")
print()
print("=========Melhor Aluno=========")
Notas = []
for i in range(7):
    Notas.append(RelacaoAlunos[i][1])
MaiorNota = max(Notas)
for i in range(7):
    if MaiorNota == RelacaoAlunos[i][1]:
        print(f"Maior nota: {MaiorNota}")
        print(f"Aluno: {RelacaoAlunos[i][0]}")
        print(f"Curso: {RelacaoAlunos[i][2]}")