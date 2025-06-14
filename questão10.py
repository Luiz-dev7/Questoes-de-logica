#preço cara da miseria
precohamburguer = 8.00
precocheeseburguer = 9.50
precofritas = 5.50
precorefrigerante = 5.00
precomilkshake = 8.00


quantidadehamburguer = int(input("Quantos hambúrgueres foram consumidos? "))
quantidadecheeseburguer = int(input("Quantos cheeseburgers foram consumidos? "))
quantidadefritas = int(input("Quantas porções de fritas foram consumidas? "))
quantidaderefrigerante = int(input("Quantos refrigerantes foram consumidos? "))
quantidademilkshake = int(input("Quantos milkshakes foram consumidos? "))

totalhamburguer = quantidadehamburguer * precohamburguer
totalcheeseburguer = quantidadecheeseburguer * precocheeseburguer
totalfritas = quantidadefritas * precofritas
totalrefrigerante = quantidaderefrigerante * precorefrigerante
totalmilkshake = quantidademilkshake * precomilkshake


totalconta = totalhamburguer + totalcheeseburguer + totalfritas + totalrefrigerante + totalmilkshake

print("\n--- Detalhamento da conta ---")
if quantidadehamburguer > 0:
    print(f"Hambúrguer(es): {quantidadehamburguer} x R${precohamburguer:.2f} = R${totalhamburguer:.2f}")
if quantidadecheeseburguer > 0:
    print(f"Cheeseburguer(es): {quantidadecheeseburguer} x R${precocheeseburguer:.2f} = R${totalcheeseburguer:.2f}")
if quantidadefritas > 0:
    print(f"Porção(ões) de Fritas: {quantidadefritas} x R${precofritas:.2f} = R${totalfritas:.2f}")
if quantidaderefrigerante > 0:
    print(f"Refrigerante(s): {quantidaderefrigerante} x R${precorefrigerante:.2f} = R${totalrefrigerante:.2f}")
if quantidademilkshake > 0:
    print(f"Milkshake(s): {quantidademilkshake} x R${precomilkshake:.2f} = R${totalmilkshake:.2f}")

print("\nTotal da conta: R$", f"{totalconta:.2f}")
