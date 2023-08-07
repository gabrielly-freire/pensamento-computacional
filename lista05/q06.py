def dias(anos, meses, dias):
    dias_final = anos*365+meses*30+dias
    return dias_final

print("Informe a idade da pessoa em anos, meses e dias")
anos = int(input("anos: "))
meses = int(input("meses: "))
dia = int(input("dias: "))

print("A pessoa já viveu {} dias".format(dias(anos, meses, dia)))

