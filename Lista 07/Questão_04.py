matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f"Digite o valor da posição ({i},{j}): ")))
    matriz.append(linha)

def MaiorColuna_MenorLinha (matriz):
    soma_colunas, soma_linhas = [0]*3, [0]*3
    for i in range(3):
        for j in range(3):
            soma_colunas[i] += matriz[j][i]
            soma_linhas[i] += matriz[i][j]
    soma_maior_coluna = max(soma_colunas)
    soma_menor_linha = min(soma_linhas)
    maior_coluna = soma_colunas.index(soma_maior_coluna)
    menor_linha = soma_linhas.index(soma_menor_linha)

    print(f"A maior coluna é a {maior_coluna+1}° coluna com a soma de seus valores igual a {soma_maior_coluna}.")
    print(f"A menor linha é a {menor_linha+1}° linha com a soma dos seus valores igual a {soma_menor_linha}.")

MaiorColuna_MenorLinha(matriz)