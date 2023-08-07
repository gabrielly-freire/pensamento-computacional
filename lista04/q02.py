n = 0
fatorial = 1

while True:
    n = int(input("Digite um numero: "))
    if n>0:
        for i in range(1,n+1):
            fatorial = fatorial*i
        print(fatorial)
        break
    else:
        print("O numero tem que ser maior que 0")
