media = float(input("Digite a média do aluno: "))

def MediaConceito(media):
    if (9 <= media <= 10):
        print("Conceito A.")
    elif (7 <= media <= 8.9):
        print("Conceito B.")
    elif (5 <= media <= 6.9):
        print("Conceito C.")
    else:
        print("Conceito D.")

MediaConceito(media)