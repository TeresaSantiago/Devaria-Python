def Validar(valido1, valido2=True):

    if valido1 and valido2:
        return "As duas variáveis são verdadeiras."
    else:
        return "Não satisfez a condição."

if __name__ == "__main__":
    teste1 = True
    # teste2 = True

    respostaDaFuncao = Validar(teste1)

    print(respostaDaFuncao)
