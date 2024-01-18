"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'

print(variavel[:5]) #até o indice 5
print(variavel[5:]) #dps do indice 5
print(len(variavel)) #qtd
print(variavel[0:9:2]) #passo
print(variavel[::-1])