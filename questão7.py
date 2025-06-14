valorporhora = float(input("Digite o valor por hora trabalhada: R$ "))
horastrabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

salario = valorporhora * horastrabalhadas


print(f"\nVocê informou que o valor por hora é R$ {valorporhora:.2f} e a quantidade de horas trabalhadas é {horastrabalhadas}.")
print(f"Portanto, o seu salário será R$ {salario:.2f}.")
