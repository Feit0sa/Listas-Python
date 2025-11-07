campeonato = []

for i in range(12):
    linha = []
    linha.append(int(input(f"Digite a posição do {i+1}° time: ")))
    linha.append(input(f"Digite o nome do {i+1}° time: "))
    linha.append(int(input(f"Digite a quantidade de pontos do {i+1}° time: ")))
    linha.append(int(input(f"Digite quantos jogos o {i+1}° time já jogou: ")))
    linha.append(int(input(f"Digite quantas vitórias teve o {i+1}° time: ")))
    linha.append(int(input(f"Digite quantos empates teve o {i+1}° time: ")))
    linha.append(int(input(f"Digite quantas derrotas teve o {i+1}° time: ")))
    print("============================================")
    campeonato.append(linha)

print(" ")
print("=====Campeão Brasileiro=====")
for i in range(12):    
    if (campeonato[i][0] == 1):
        print(campeonato[i][1])
print("============================\n")

print("=====Classificados para a Libertadores=====")
for i in range(12):
    if (campeonato[i][0] <= 5):
        print(campeonato[i][1])
print("===========================================\n")        

print("=====Classificados para a Copa Sul-Americana=====")
for i in range(12):
    if (6 <= campeonato[i][0] <= 10):
        print(campeonato[i][1])
print("=================================================\n")    
    
print("=====Rebaixados para a Série B=====")
for i in range(12):
    if (campeonato[i][0] > 10):
        print(campeonato[i][1])
print("===================================\n")