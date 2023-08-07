lista = ['julio', 'anna', 'isabel', 'izaac', 'eduardo']

for nome in lista:
    print(nome)

nome = input("Qual nome você quer verificar? ")

if nome in lista:
    print("O nome {} está na lista!".format(nome))
else:
    print("O nome {} não está na lista!".format(nome))
