salario = float(input("Qual seu salario: "))
financiamento = float(input("Qual seu financiamento: "))

if financiamento/salario <= 5:
    print("Financiamento concedido")
else:
    print("Financiamento negado")
print("Obrigado por nos consultar")
