# Fatiamento de strings
#  012345678
#  Olá mundo
# -987654321
# Fatiamento [i:f:p] 'i = início, f = fim, p = passo' [::]
# Obs.: a função len retorna a quantidade de caracteres da str
# O índice final é omitido
variavel = 'Olá mundo'

print(variavel[5])
print(variavel[-4])
print(variavel[4:])
print(f'A palavra "{variavel}" tem {len(variavel)} caracteres.')

# Para inverter uma string usando fatiamento
print(variavel[::-1])
