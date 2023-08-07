def divisores(n):
    cont = 0
    for i in range(1, n+1):
        if n%i==0:
            cont=cont+1
    return cont

n = int(input("Qual número gostaria de checar os divisores? "))
print("O número {} tem {} divisores.".format(n, divisores(n)))