altura=float (input ("Sua altura: "))
peso=float (input ("seu peso em kg: "))
imc = peso/ (altura**2)
print ("O seu imc é: ",round(imc,2))

if imc>35:
    print("você está forte")
if imc<35:
    print("você está magro")

