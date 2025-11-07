valor_saque = int(input("Digite o valor do saque: "))

def saque_min (valor):
    cedulas = {200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0}
    if (valor == 3 or valor == 1):
        print("Valor para saque indisponível.")
    else:
        for i in cedulas:
            while (valor >= i):
                if (valor == 13 or valor == 11):
                    valor -= 5
                    cedulas[5] += 1
                elif (valor == 8 or valor == 6):
                    valor -= 2
                    cedulas[2] += 1 
                elif (valor >= i):
                    valor -= i
                    cedulas[i] += 1
        print("Saque realizado com sucesso!")
        for i in cedulas:
            quantidades = cedulas[i]
            if (quantidades > 0):
                print(f"{quantidades} cédula(s) de {i} reais")
    

saque_min(valor_saque)