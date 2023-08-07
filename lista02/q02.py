
print("Digite quatro numeros:")

lista = []

for i in range(4):
    lista.append(int(input()))

maior = -2147483647
menor = 2147483647

for n in lista:
    if n > maior:
        maior = n
    if n < menor:
        menor=n

print("Maior número é o ", maior)
print("Menor número é o ", menor)
