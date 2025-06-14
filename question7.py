while True:
    idade = int(input("Digite a sua idade em anos: "))

    if idade <= 0:
        print("Idade inválida! Por favor, digite um número maior que zero.")
    else:
        break 


if idade == 1:
    idade_cao = 10.5
elif idade == 2:
    idade_cao = 21
else:
    idade_cao = 21 + (idade - 2) * 4

print(f"Se você fosse um cão, teria {idade_cao} anos.")
