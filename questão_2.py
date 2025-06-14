while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        if numero > 0:
            print("O número é positivo.")
        elif numero < 0:
            print("O número é negativo.")
        else:
            print("O número é zero.")
        break  
    except ValueError:
        print("Erro: por favor, digite um número inteiro válido.")

