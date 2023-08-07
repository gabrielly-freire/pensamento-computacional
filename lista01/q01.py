valor_litro = float(input("Qual o valor do combustível?"))
valor = float(input("Quanto você quer abastecer (apenas número)?"))

qtd = valor/valor_litro

print("A quantidade abastecida é %.2f Litros"%(qtd))