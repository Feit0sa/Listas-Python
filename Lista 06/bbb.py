matriz = []

lado = int(input("Digite o tamanho do lado da mtriz: "))

for i in range(lado):
    linha = []
    for j in range(lado):
        linha.append(int(input(f"Digite o valor da posição ({i},{j}): ")))
    matriz.append(linha)

print(" ")
for i in range(lado):
    print(matriz[i])


