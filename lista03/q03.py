lista = []

print("Os nomes da lista são:")
for i in range(0,5):
    lista.append(input())

nome = input("Qual nome deseja apagar? ")

if nome in lista:
   # lista.pop(i)  remove com index indicado
    lista.remove(nome) # remove com valor indicado
    print("{} foi apagado da lista!".format(nome))
else:
    print("{} não foi encontrado na lista!".format(nome))

print("A lista atual é: ")

for i in lista:
    print(i)