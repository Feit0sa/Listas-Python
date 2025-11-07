# Algoritmo para números com repetição
from random import randint

vetor, posicoes = [randint(1, 10) for i in range(10)], {}
print(vetor)

for i, num in enumerate(vetor):
    if num in posicoes:
        posicoes[num].append(i)
    else:
        posicoes[num] = [i]

number = int(input("Selecione um número para ver a sua posição: "))

if number in posicoes:
    indices = posicoes[number]
    if (len(indices) > 1):
        print(f"O {number} aparece nas posições: {indices}")
    else:
        print(f"O {number} aparece na posição: {indices}")
else:
    print(f"O número {number} não aparece na lista.")