user = password = ""

while user == password:
    user = input("Digite o usuário: ")
    password = input("Digite a senha: ")
    if user != password:
        print("Senha válida")
    else:
        print("A senha nao pode ser igual ao nome do usuário")

