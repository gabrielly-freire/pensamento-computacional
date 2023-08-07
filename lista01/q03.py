valor_divida = float(input("Quanto é o valor inicial da dívida? "))
valor_multa = float(input("Quanto é o valor de multa por dia de atraso?"))
dias = int(input("Quantos dias está em atraso?"))

divida_final = (valor_multa*dias)+valor_divida

print("O valor da dívida é R$ ",divida_final)