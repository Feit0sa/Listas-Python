# Crie uma função recursiva que receba uma string e imprima todas as permutações possíveis dos seus caracteres.

def anagramas(string):
    resultado = []
    if (len(string) == 0):
        return [""]
    for i in range(len(string)):
        letra = string[i]
        restante = string[:i]+string[i+1:]
        for j in anagramas(restante):
            resultado.append(letra+j)
    return resultado
    
print(anagramas("abc"))