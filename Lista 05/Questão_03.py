from random import randint

nums, primos = [], []
sorteado = 0

for i in range(10):
    while True:
        sorteado = randint(0, 100)
        repetido = False
        for j in range(i-1):
            if (nums[j] == sorteado):
                repetido = True
        if (repetido == False):
            break
    nums.append(sorteado)

for i in range(10):
    primo = 0
    for j in range(2, nums[i]):
        if (nums[i] % j == 0):
            primo += 1
    if (primo == 0 and nums[i] != 1 and nums[i] != 0):
        primos.append(nums[i])    

primos.sort()
print(f"Lista de números aleatórios: {nums}")
print(f"Esses são os números primos: {primos}")
print(f"A quantidade é {len(primos)}")