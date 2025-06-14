from datetime import datetime
while True:
    try:
        data_nascimento = input("Digite a sua data de nascimento (formato dd/mm/aaaa): ")
        nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
        hoje = datetime.now() 
        idade = hoje.year - nascimento.year
        if hoje.month < nascimento.month or (hoje.month == nascimento.month and hoje.day < nascimento.day):
            idade -= 1  
        if idade >= 18:
            print("Você pode assinar a documentação.")
        else:
            print("A documentação precisa ser assinada por seu responsável legal.")
        break  
    except ValueError:
        print("Data de nascimento inválida. Por favor, use o formato dd/mm/aaaa.")
