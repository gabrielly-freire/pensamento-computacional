lista = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio','junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

n = int(input("Qual o número do mês?"))
if n >=1 and n<=12:
    print("O mês é ", lista[n-1])
else:
    print("Não existe mes de número {}!".format(n))
