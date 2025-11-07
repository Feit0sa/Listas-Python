# Faça uma função em python para gerar um vetor de 10 valores inteiros e informar o maior valor deste, recursivamente.
from random import randint

def maior(num = [], count = 1):
    num.append(randint(1, 10))
    if (count == 10):
        return max(num), num
    return maior(num, count+1)

print(maior())