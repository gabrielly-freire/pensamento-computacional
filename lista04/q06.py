print("Digite 5 números:")

lista = []

for i in range(0,5):
    lista.append(int(input()))   

"""for i in range(1,5):
    if lista[i-1]>lista[i]:
        aux = lista[i]
        lista[i]=lista[i-1]
        lista[i-1]=aux"""

for i in range(1,5):
    if lista[i-1]>lista[i]:
        n1 = lista[i]
        n2 = lista[i-1]
    else:
        n1 = lista[i-1]
        n2 = lista[i]
    string="intervalo [{}, {}]= ".format(n1, n2)
    for j in range(n1, n2+1):
        string=string+str(j)+", "
    print(string[0:len(string)-2])

print(lista) 
