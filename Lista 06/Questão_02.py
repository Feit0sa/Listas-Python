funcionarios = []

for i in range(4):
    linha = []
    linha.append(int(input(f"Digite a matrícula do {i+1}° funcionário: ")))
    linha.append(input(f"Digite o nome do {i+1}° funcionário: "))
    linha.append(input(f"Digite a a função do {i+1}° funcionário: "))
    linha.append(int(input(f"Digite o salário do {i+1}° funcionário: ")))
    funcionarios.append(linha)

for i in range(4):
    print(funcionarios[i])