"""
Introdução ao empacotamento e desempacotamento
"""
primeiro, _, nome, *resto = ['Becca', 'Rose', 'João Victor', 'Arara']
print(nome)
print(primeiro)
print(_)
print(resto)

# Desempacotamento estendido
a, *resto = [1, 2, 3, 4, 5]
print(a)  # Saída: 1
print(resto)  # Saída: [2, 3, 4, 5]
