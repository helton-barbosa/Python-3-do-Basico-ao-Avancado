# Em Python, a função embutida range() é comumente usada em conjunto com a
# estrutura de controle for para criar uma sequência de números. Aqui está uma
# explicação detalhada com exemplos:

# Função range():
# A função range() é usada para gerar uma sequência de números. Pode receber
# um, dois ou três argumentos:
"""
1 - range(stop): Gera uma sequência de números de 0 até (stop - 1).
2 - range(start, stop): Gera uma sequência de números de start até (stop - 1).
3 - range(start, stop, step): Gera uma sequência de números de start até
    (stop - 1) com um intervalo de step entre os números.
"""

# Sequência de 0 a 4
for i in range(5):
    print(i)
# Saída: 0, 1, 2, 3, 4

# Sequência de 2 a 6
for i in range(2, 7):
    print(i)
# Saída: 2, 3, 4, 5, 6

# Sequência de 0 a 10 com incremento de 2
for i in range(0, 11, 2):
    print(i)
# Saída: 0, 2, 4, 6, 8, 10

# Notas adicionais:
# A função range() é inclusiva no início e exclusiva no final, o que significa
# que o valor final não é incluído na sequência.
# range() é útil para gerar índices em loops for ou criar listas de números.
# Você pode usar a função list() para converter um objeto range em uma lista.
