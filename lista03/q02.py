import random

lista = []

for i in range(0,5):
    ale = random.randrange(1, 100)
    lista.append(ale)

for n in lista:
    if n%2==0:
        print("O número {} é par".format(n))
    else:
        print("O número {} é ímpar".format(n))