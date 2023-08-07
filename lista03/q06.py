import random

lista = []
for i in range(0, 10):
    ale = random.randrange(1,6)
    lista.append(ale)

print("A lista é:")
for i in range(0,10):
    print(lista[i])

print("Após encontrar os números 5 a lista ficou:")
for i in range(0,10):
    if lista[i]==5:
        lista[i]="CINCO"
    print(lista[i])



