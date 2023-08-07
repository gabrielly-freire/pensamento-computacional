def fatorial(n):
    fatorial = 1
    for i in range(1, n+1):
        fatorial = fatorial*i
    print("{}! é {}".format(n, fatorial))

n = int(input("Qual numero você gostaria de saber o fatorial? "))
if (n>=0):
    fatorial(n)
else:
    print("Digite um valor positivo")