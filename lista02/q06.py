valor = float(input("Valor de compra: "))
opcao = input("Opçao de pagamento: ")

if opcao == 'V':
    valor = valor*0.95
    print("Valor a ser pago - ", valor)
elif opcao == 'P':
    valor = valor*1.08
    print("Valor a ser pago = {} em 3 parcelas de {}".format(valor, valor/3))
