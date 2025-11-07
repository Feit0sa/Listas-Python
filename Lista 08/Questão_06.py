from random import randint
def soma_naturais(num):
    if (num == 0):
        return 0
    else:
        return num+soma_naturais(num-1)
    
print(soma_naturais(randint(1, 10)))