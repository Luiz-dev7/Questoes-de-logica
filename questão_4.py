nota1= float(input("Nota 1: "))
nota2= float(input("Nota 2: "))
nota3= float(input("Nota 3: "))
media= (nota1 + nota2 + nota3) / 3
print("Média:", media)
if media== 10:
    print("Aprovado com distinção")
elif media>= 7:
    print("Aprovado")
else:
    print("Reprovado")
