salario = float(input("Qual o salário atual?"))
porcentagem_ajuste = float(input("Qual a porcentagem de ajuste? "))

reajuste = salario*porcentagem_ajuste/100
salario_final = reajuste+salario

print("O reajuste foi de {} reais e {} centavos".format(int(reajuste),int((reajuste-int(reajuste))*100)))
print("O valor final do salário é {} rais e {} centavos".format(int(salario_final),int((salario_final-int(salario_final))*100)))
