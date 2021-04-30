if __name__ == "__main__":
    nota = int(input("Difite sua nota:"))

    if nota <= 30:
        print("Você foi reprovado!!!")
    elif nota <= 60:
        print("Você ficou de Prova Final!!!")
    else:
        print("Você está aprovado")