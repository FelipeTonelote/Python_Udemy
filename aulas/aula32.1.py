"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um número: ')

try:
    numero_int = int(numero)
    par = (numero_int % 2) == 0
    if par:
        print('O número {} é par'.format(numero))
    else: 
        print('O número {} é ímpar'.format(numero))          
except:
        print('Não é um número inteiro')
