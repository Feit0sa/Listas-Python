clientes = []

for i in range(5):
    linha = []
    linha.append(input(f'Digite o número da conta do {i+1}° cliente: '))
    linha.append(input(f'Digite o nome do {i+1}° cliente: '))
    linha.append(int(input(f'Digite o saldo do {i+1}° cliente: ')))
    linha.append(input(f'Digite a operação bancária do {i+1}° cliente: '))
    linha.append(int(input(f'Digite o valor da operação do {i+1}° cliente: ')))
    clientes.append(linha)

for i in range(5):
    print(clientes[i])