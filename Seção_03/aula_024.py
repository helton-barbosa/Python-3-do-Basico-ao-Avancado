# Os operadores in e not in em Python são utilizados para verificar a presença
# de um valor em uma sequência (como uma lista, tupla, string, conjunto ou
# dicionário). Aqui está uma explicação detalhada com exemplos:

# Operador in:
# O operador in verifica se um valor está presente em uma sequência. Ele
# retorna True se o valor estiver presente e False caso contrário.

# Exemplo com Lista:
lista = [1, 2, 3, 4, 5]
print(3 in lista)  # Saída: True
print(6 in lista)  # Saída: False

# Exemplo com String:
frase = "Olá, mundo!"
print('m' in frase)  # Saída: True
print('x' in frase)  # Saída: False

# Operador not in:
# O operador not in verifica se um valor não está presente em uma sequência.
# Ele retorna True se o valor não estiver presente e False caso contrário.

# Exemplo com Tupla:
tupla = (10, 20, 30, 40, 50)
print(25 not in tupla)  # Saída: True
print(40 not in tupla)  # Saída: False

# Exemplo com Dicionário (verifica chaves):
dicionario = {'a': 1, 'b': 2, 'c': 3}
print('b' not in dicionario)  # Saída: False
print('z' not in dicionario)  # Saída: True

# Utilização em Estruturas Condicionais:
frutas = ['maçã', 'banana', 'laranja', 'uva', 'pitanga']
if 'pitanga' in frutas:
    print("A pitanga está na lista de frutas.")
else:
    print("A pitanga não está na lista de frutas.")
# Neste exemplo, o operador in é utilizado para verificar se 'laranja' está na
# lista de frutas. Como está presente, a mensagem "A laranja está na lista de
# frutas." será impressa.

# Os operadores in e not in são úteis para verificar a presença ou ausência de
# valores em estruturas de dados. Eles oferecem uma forma simples e concisa de
# realizar essa verificação em diversas situações de programação. Certifique-se
# de compreender bem como funcionam e utilize-os conforme necessário em seu
# código.
