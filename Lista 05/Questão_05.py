vetor = []

for i in range(10, 21):
    if (i % 2 == 0):
        vetor.append(i)

vetor.sort(reverse=True)
print(vetor)