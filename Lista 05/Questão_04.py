sequencia = []
termo = 1
termo_anterior = 0
for i in range(20):
    sequencia.append(termo)
    termo += termo_anterior
    termo_anterior = termo - termo_anterior

print(sequencia)