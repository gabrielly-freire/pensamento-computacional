
# Lista 2 - Condicionais

## Questão 1

Fazer um algoritmo para ler a idade da pessoa, verificar e mostrar se ela já tem idade para votar (16 anos ou mais) e para conseguir a Carteira de Habilitação (18 anos ou mais).

**Exemplo:**

```
Qual sua idade? 17
Tem idade para votar
Não tem idade para dirigir
```

## Questão 2

Escrever um algoritmo para ler quatro valores inteiros e escrever na tela o maior e o menor deles.

**Exemplo:**

Entrada:
```
Digite quatro números:
4
5
10
20
```

Saída:
```
Maior número é o 20
Menor número é o 4
```

## Questão 3

Elaborar um algoritmo que receba o valor do salário de uma pessoa e o valor de um financiamento pretendido. Caso o financiamento seja menor ou igual a 5 vezes o salário da pessoa, o algoritmo deverá escrever “Financiamento Concedido"; senão, ele deverá escrever "Financiamento Negado". Independente de conceder ou não o financiamento, o algoritmo escreverá depois a frase "Obrigado por nos consultar."

**Exemplo 1:**

```
Qual seu salário: 10.000
Qual seu financiamento: 100.000
Resposta:
Financiamento Negado
Obrigado por nos consultar
```

**Exemplo 2:**

```
Qual seu salário: 10.000
Qual seu financiamento: 40.000
Resposta:
Financiamento Concedido
Obrigado por nos consultar
```

## Questão 4

Elaborar um programa que efetue a leitura do nome e do sexo de uma pessoa, apresentando como saída uma das seguintes mensagens: "Ilmo Sr.", se o sexo informado for masculino, ou a mensagem "Ilma Sra.", para o sexo informado como feminino. Apresente também junto da mensagem de saudação o nome previamente informado.

**Exemplo 1:**

```
Qual seu nome: Anna
Qual seu sexo: Feminino
Saída: Ilma Sra. Anna
```

**Exemplo 2:**

```
Qual seu nome: Júlio
Qual seu sexo: Masculino
Saída: Ilmo Sr. Júlio
```

## Questão 5

Faça um programa que simule um caixa eletrônico. É exibido um menu com as seguintes opções: 1 SAQUE, 2 DEPÓSITO, 3 SALDO. O saldo da conta deve ser definido no início do programa como R$ 1000,00. O usuário ao selecionar a opção SAQUE será perguntado pelo valor que deseja sacar. Se for abaixo de 1000,00, autorizar o saque e exibir o saldo restante. Se for acima de R$ 1000,00 mostrar uma mensagem de saldo insuficiente. Na opção DEPÓSITO o programa pergunta o valor a ser depositado. Se o valor for positivo, adicionar ao saldo existente e mostrar na tela o novo saldo. Se for um valor negativo, exibir mensagem de valor inválido. Para a opção SALDO, o programa exibe o saldo atual e agradece ao usuário por usar os serviços do banco.

## Questão 6

Fazer um programa que leia o valor de uma compra e a opção de pagamento (V – para pagamento à vista ou P – para pagamento parcelado). Caso o cliente pague à vista terá um desconto de 5%, caso pague em 3 vezes terá um acréscimo de 8%. O programa deve mostrar o valor da compra e o valor à vista ou valor a prazo (valor total e o valor de cada parcela).

**Exemplo 1:**

```
Valor de compra: 10.000
Opção de pagamento: V
Saída: Valor a ser pago = 9500
```

**Exemplo 2:**

```
Valor de compra: 10.000
Opção de pagamento: P
Saída: Valor a ser pago = 10.800 em 3 parcelas de 3600
```
