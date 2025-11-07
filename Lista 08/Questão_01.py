def fibonacci (termo = 1, termo_anterior = 0, contador = 1):
    print(termo)
    if (contador == 12):
        return termo
    fibonacci(termo+termo_anterior, termo, contador+1)

fibonacci()