# Em Python, você pode usar a cláusula else junto com um loop while para
# executar um bloco de código quando a condição do loop se torna falsa. Aqui
# está uma explicação detalhada com exemplos:

# Sintaxe:
"""
while condição:
    # Bloco de código a ser executado enquanto a condição for verdadeira
else:
    # Bloco de código a ser executado quando a condição se tornar falsa
"""

contador = 0
while contador < 5:
    print(f'Contagem: {contador}')
    contador += 1
else:
    print(f'Loop concluído! Mas não mostrei o valor {contador}')

# O loop while é executado enquanto a condição (contador < 3) for verdadeira.
# O bloco de código dentro do loop é executado para cada iteração enquanto a
# condição é verdadeira.
# Quando a condição se torna falsa (ou seja, contador >= 3), o bloco de código
# dentro do else é executado.
