matriz = []
linhas_iguais, colunas_iguais, diagonais_iguais = False, False, False

lado = int(input("Digite o tamanho do lado da mtriz: "))
for i in range(lado):
    linha = []
    for j in range(lado):
        linha.append(int(input(f"Digite o valor da posição ({i},{j}): ")))
    matriz.append(linha)

soma_linhas = [0]*lado
soma_colunas = [0]*lado
soma_diagonais = [0, 0]
for i in range(lado):
    for j in range(lado):
        soma_linhas[i] += matriz[i][j]
        soma_colunas[i] += matriz[j][i]
        soma_diagonais[0] += matriz[i][i]
        soma_diagonais[1] += matriz[i][lado-1-i]

# uma lista vazia é equivalente a false, então num if(lista) e a lista estiver vazia, retorna false, se tiver algum valor, retorna true
if (all(i == soma_linhas[0] for i in soma_linhas)):
    linhas_iguais = True
if (all(i == soma_colunas[0] for i in soma_colunas)):
    colunas_iguais = True
if (all(i == soma_diagonais[0] for i in soma_diagonais)):
    diagonais_iguais = True
if (linhas_iguais and colunas_iguais and diagonais_iguais):
    print("A matriz é um quadrado mágico.")
else:
    print("A matriz NÃO é um quadrado mágico")

print("=====Matriz=====")
for i in range(lado):
    print(matriz[i])