from random import randint # Importa classe para gerar números aleatórios
vetor = [randint(1, 10) for i in range(10)] # Cria o vetor e gera 10 valores aleatórios
repetidos = [] # Declara array vazio
posicoes = {} # Cria um dicionário
repeticoes = 0 # Declara a variável "repeticoes"

# Preenche o dicionário com as posições em que os números do vetor aparecem
for i, num in enumerate(vetor):
    if (num in posicoes):
        posicoes[num].append(i)
    else:
        posicoes[num] = [i]

# Caso as chaves do dicionário tenham mais de uma posição, irá acrescentar +1 na variaável repetições e armazena os números repetidos no array "repetidos"
for chave in posicoes:
    indices = posicoes[chave]
    if (len(indices) > 1):
        repeticoes += len(indices)
        repetidos.append(chave)

print(f"A lista de números aleatórios é: {vetor}")
print(f"Existem {repeticoes} números repetidos e são os números: {repetidos}")