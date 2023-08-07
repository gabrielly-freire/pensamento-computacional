km_inicial = int(input("Qual o valor da kilometragem inicial? "))
km_final = int(input("Qual o valor da kilometragem final? "))
litros = float(input("Quantos litros foram consumidos na viagem?"))

consumo = (km_final-km_inicial)/litros

print("O valor de consumo médio é de: %.2f Km/L"%(consumo))