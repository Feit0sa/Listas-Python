# Faça uma função em python para ler um valor n qualquer e, em seguida, calcular e informar a função exponencial (2^n) deste valor, recursivamente.
from random import randint
def exponencial(num):
    if (num == 0):
        return 1
    else:
        return 2*exponencial(num-1)

print(exponencial(randint(1, 10)))