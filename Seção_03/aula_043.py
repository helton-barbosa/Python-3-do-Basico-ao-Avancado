# Em Python, a estrutura de controle for é usada para iterar sobre uma
# sequência (como uma lista, tupla, dicionário, conjunto ou string) ou outro
# objeto iterável. O operador in é usado em conjunto com for para percorrer os
# elementos dessa sequência. Aqui está uma explicação detalhada com exemplos:

# Sintaxe básica do for com in:
"""
for elemento in sequência:
    # Bloco de código a ser executado para cada elemento na sequência
"""

# Exemplo com lista:
frutas = ['maçã', 'banana', 'laranja', 'tamarindo', 'morango', 'pitomba']
for fruta in frutas:
    print(fruta)

# Exemplo com string:
palavra = 'Nabucodonosor'
for letra in palavra:
    print(letra)

# Exemplo com range():
for cont in range(15):
    print(cont)

# Exemplo com dicionário:
pessoa = {'nome': 'Helton', 'idade': 38, 'cidade': 'Palmas'}
for chave in pessoa:
    print(chave, pessoa[chave])

# Uso do enumerate():
frutas = ['maçã', 'banana', 'laranja', 'tamarindo', 'morango', 'pitomba']
for indice, fruta in enumerate(frutas):
    print(f'Índice {indice}: {fruta}')

# Notas adicionais:
# O for em Python é usado para iterar sobre qualquer objeto iterável, como
# listas, strings, dicionários, conjuntos, etc.
# O operador in é usado para verificar se um elemento está presente na
# sequência.
# O for pode ser usado com a função range() para gerar uma sequência de números
# O for também pode ser combinado com a função enumerate() para obter índices e
# valores ao iterar sobre uma sequência.
