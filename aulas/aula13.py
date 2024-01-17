nome = input('Qual é o seu nome? ')
altura = float(input('Qual é a sua altura em metros? '))
peso = int(input('Qual é o seu peso em KG? '))

#CALCULANDO IMC
calculoIMC = peso / (altura * altura)

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} e seu IMC é:'
linha_3 = f'{calculoIMC:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)