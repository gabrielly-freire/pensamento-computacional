nome = input("Qual seu nome: ")
sexo = input("Qual seu sexo: ")

if sexo == "Feminino":
    print("Ilma Sra. ", nome)
elif sexo == "Masculino":
    print("Ilm Sr. ", nome)
else:
    print("Desconhecido")