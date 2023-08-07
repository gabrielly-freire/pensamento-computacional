import datetime

nome = input("Qual seu nome? ")
ano_nascimento = int(input("Qual seu ano de nascimento? "))

data = str(datetime.date.today())

ano = int(data[0:4])

print("{} tem {} anos".format(nome, ano-ano_nascimento))