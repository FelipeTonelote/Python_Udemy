"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input('Digite a hora em números inteiros: ')

try:
    hora_int = int(hora)
    if 0 <= hora_int <= 11: 
        print('Bom dia')
    elif 12 <= hora_int <=17:
        print('Boa tarde')
    elif 18 <= hora_int <= 23:
        print('Boa noite')
    else:
        print('Digite uma hora válida (0-23)')
except:
    print('Por favor, digite um número inteiro')