peso = float(input("Digite o seu peso em Kg: "))
altura = float(input("Digite a sua altura em metros: "))

def IMC (peso, altura):
    imc = peso / (altura**2)
    if (imc >= 40):
        print("Classificação: Obesidade Grave")
        print("Obesidade (Grau): III")
    elif (30 <= imc <= 39.9):
        print("Classificação: Obesidade")
        print("Obesidade (Grau): II")
    elif (25 <= imc <= 29.9):
        print("Classificação: Sobrepeso")
        print("Obesidade (Grau): I")
    elif (18.5 <= imc <= 24.9):
        print("Classificação: Normal")
        print("Obesidade (Grau): 0")
    else:
        print("Classificação: Magreza")
        print("Obesidade: 0")

IMC(peso, altura)