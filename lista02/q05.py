print("1 SAQUE, 2 DEPÓSITO, 3 SALDO.")
opcao = int(input("Escolha uma operação: "))
saldo = 1000.0

if opcao == 1:
	valor = float(input("Digite o valor do saque: "))
	if valor <= saldo:
		saldo = saldo - valor
		print("Seu saldo é ", saldo)
	else:
		print("Saldo insuficiente")
elif opcao == 2:
	valor = float(input("Digite o valor do deposito: "))
	if valor > 0:
		saldo = saldo + valor
		print("Seu saldo é ", saldo)
	else:
		print("Valor inválido")
elif opcao == 3:
	print("Seu saldo é ", saldo)
	print("Obrigado por nos consultar")
else:
	print("operação desconhecida")
