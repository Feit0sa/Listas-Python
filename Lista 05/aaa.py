lista = [4, 2, 7, 2, 9, 4, 2]

# Construir o dicionário com as posições de todos os números
posicoes = {}
for i, num in enumerate(lista):
    if num in posicoes:
        posicoes[num].append(i)
    else:
        posicoes[num] = [i]

print(lista)
# Perguntar ao usuário qual número ele quer verificar
numero_verificar = int(input("Digite o número que deseja verificar: "))

# Verificar se o número está no dicionário e se aparece mais de uma vez
if numero_verificar in posicoes:
    indices = posicoes[numero_verificar]
    if len(indices) > 1:
        print(f"O número {numero_verificar} aparece nas posições: {indices}")
    else:
        print(f"O número {numero_verificar} aparece apenas uma vez, na posição {indices[0]}")
else:
    print(f"O número {numero_verificar} não aparece na lista.")

print(posicoes)
