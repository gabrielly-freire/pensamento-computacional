lista = []

print("Digite 10 número: ")
for i in range(0,10):
    lista.append(int(input()))
soma = 0
for n in lista:
    soma = soma + n
media = soma/10.0
print("A média é: ", media)

print("Os números à cima da média são:")
for n in lista:
    if n > media:
        print(n)