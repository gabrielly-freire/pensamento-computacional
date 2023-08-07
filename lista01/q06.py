salario = float(input("Qual o valor do seu salário? "))
despesa = float(input("Qual sua despesa mensal? "))

tempo = (1000000/(salario - despesa))/12

print("Você vai demorar {} anos e {} meses para poupar milhão".format(int(tempo), round((tempo-int(tempo))*12)))