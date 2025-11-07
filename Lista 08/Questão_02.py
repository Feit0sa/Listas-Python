from random import randint

matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(randint(1, 10))
    matriz.append(linha)

def soma_diagonais3x3 (matriz, soma_diagonais = [0, 0]):
    for i in range(3):
        soma_diagonais[0] += matriz[i][i]
        soma_diagonais[1] += matriz[i][3-1-i]
    return soma_diagonais

print(soma_diagonais3x3(matriz))
print(matriz) # Para conferir resultados