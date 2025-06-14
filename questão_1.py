while True:
    try:
        numero1 = int(input("Digite o primeiro número inteiro: "))
        numero2 = int(input("Digite o segundo número inteiro: "))
        
        if numero1 == numero2:
            print("Os números são iguais.")
        else:
            menor = min(numero1, numero2)
            print("O número menor é:", menor)
        break  
    except ValueError:
        print("Por favor, digite um número inteiro válido.")
