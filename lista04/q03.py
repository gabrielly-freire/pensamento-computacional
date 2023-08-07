n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

if n1>n2:
    aux = n1
    n1 = n2
    n2 = aux
lista = []
for i in range (n1+1, n2):
    if i%2==0:
        lista.append(i)

string = ""
for i in lista:
    string = string+str(i)+", "

print("saida:", string[0:len(string)-2])
