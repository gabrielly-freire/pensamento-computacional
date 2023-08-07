def triangulo(lados):
    n=0
    if lados[0]+lados[1]<=lados[2] or lados[0]+lados[2]<= lados[1] or lados[1]+lados[2]<=lados[0]:
        n=0
    elif  lados[0]==lados[1]==lados[2]:
        n = 1
    elif lados[0]==lados[1] or lados[0]==lados[2]or lados[1]==lados[2]:
         n= 2
    else:
        n = 3

    return n

print("Informe os lados")
lados = []
for i in range(0, 3):
    lados.append(int(input()))
tipo = triangulo(lados)

match tipo:
    case 0:
        tipo = "não é triangulo"
    case 1:
        tipo = "equilátero"
    case 2:
        tipo = "isósceles"
    case 3:
        tipo = "escaleno"

print("Os lados {} representam um triangulo do tipo {}".format(lados, tipo))