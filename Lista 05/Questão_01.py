from random import randint

nums = []

for i in range(10):
    nums.append(randint(1, 101))

print(f"Números sorteados: {nums}")

nums.sort()
print(f"A lista de números sorteados organizados de forma crescente fica assim: {nums}")
nums.sort(reverse=True)
print(f"A lista de números sorteados organizados de forma decrescente fica assim: {nums}")