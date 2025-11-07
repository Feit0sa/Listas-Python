n = int(input('Digite a dimensão n da matriz: '))
m = int(input('Digite a dimensão m da matriz: '))
matriz = []
for i in range(n):
  linha = []
  for j in range(m):
    linha.append(int(input('Digite o valor de ['+ str(i) + ',' + str(j) + ']:')))
  matriz.append(linha)

for i in range(n):
  print(matriz[i])