def media(lista, tipo):
    soma = 0
    peso = [5,3,2]
    for i in range(0,3):
        if tipo == 'A':
            soma = lista[i] + soma
            media = soma/3
        else:
            soma = lista[i]*peso[i]+soma
            media = soma/10

    return media

lista = []

print("Quais são as notas?")
for i in range(0,3):
    lista.append(int(input()))

tipo = input("Que tipo de média você quer? ")
print("A média é: ", media(lista, tipo))