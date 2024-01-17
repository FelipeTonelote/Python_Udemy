nome = input('Qual é o seu nome? ')
altura = float(input('Qual é a sua altura em metros? '))
peso = int(input('Qual é o seu peso em KG? '))

#CALCULANDO IMC
calculoIMC = peso / (altura * altura)

print(nome, 'tem', altura, 'de altura,\n', 'pesa', peso, 'e seu IMC é:\n', calculoIMC)