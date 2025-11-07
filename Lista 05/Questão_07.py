from random import randint
vetor = [randint(1, 10) for i in range(10)]
pares, impares = 0, 0

for i in range(10):
    if (vetor[i] % 2 == 0):
        pares += 1
    elif (vetor[i] % 2 == 1):
        impares += 1

print(vetor)
print(f"Existem {pares} números pares e {impares} números ímpares")