
while True:
    n = int(input("Digite 1 numero:"))
    if not(n>=1 and n<=9):
        print("O numero precisa ser entre 1 e 9")
    else:
        for i in range(1, 10):
            print("{}x{}= {}".format(n, i, n*i))
        break
