def paridade(n):
    if n % 2 == 0:
        print("{} é par".format(n))
    else:
        print("{} é ímpar".format(n))

n = int(input("Qual valor você quer testar? "))
paridade(n)