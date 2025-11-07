vetor1, vetor2, vetor3 = [], [], []

for i in range(21):
    if (i % 2 == 0 and i >= 2):
        vetor1.append(i*i)
    if (i > 9 and i < 20):
        vetor2.append(i)

print(f"Lista dos quadrados dos múltiplos de 2 no intervalo 2 a 20: {vetor1}")
print(f"Lista de números no intervalo de 10 a 19: {vetor2}")

for i in range(10):
    vetor3.append(vetor1[i]+vetor2[i])

print(f"Lista da soma das duas listas anteriores: {vetor3}")