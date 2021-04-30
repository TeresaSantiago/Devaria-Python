if __name__ == "__main__":
    listaConvidados = ["Teresa", "Cristian", "Carlos"]

    nome = input("Digite seu nome:")
    idade = int(input("Digite a sua idade:"))

    estaNaLista = nome in listaConvidados
    maiorIdade = idade >= 18

    if estaNaLista:
        if maiorIdade:
            print("Pode entrar, você foi convidado e é maior de idade!!!")
        else:
            print("Desculpe, mas seu nome está na lista, mas você não é maior de idade!!!")
    else:
        print("Desculpe, mas seu nome não estpa na lista!!!")
