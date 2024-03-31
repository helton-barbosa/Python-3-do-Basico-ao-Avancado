# As f-strings (formatted string literals) em Python são uma maneira
# conveniente e legível de formatar strings de maneira dinâmica, introduzidas
# a partir da versão 3.6 do Python. Elas permitem incorporar expressões Python
# dentro de strings, o que simplifica significativamente a formatação de texto.
# Aqui está uma explicação detalhada com exemplos:

# Sintaxe das f-strings:
# As f-strings são strings prefixadas pelo caractere f, seguido por aspas
# simples ou duplas. Dentro da f-string, você pode incluir expressões Python
# entre chaves {} para que sejam avaliadas e inseridas na string resultante.

# Exemplos:
nome = "Alice"
idade = 30

# Exemplo básico
mensagem = f"Olá, meu nome é {nome} e eu tenho {idade} anos."
print(mensagem)  # Saída: Olá, meu nome é Alice e eu tenho 30 anos.

# Expressões Python
numero = 10
mensagem = f"O dobro de {numero} é {numero * 2}."
print(mensagem)  # Saída: O dobro de 10 é 20.

# Chamadas de métodos
frase = "python é divertido"
mensagem = f"A frase tem {len(frase)} caracteres."
print(mensagem)  # Saída: A frase tem 19 caracteres.

# Formatação de números
preco = 19.99
mensagem = f"O preço é R$ {preco:.2f}."
print(mensagem)  # Saída: O preço é R$ 19.99.

# Expressões Complexas:
# Você também pode incluir expressões Python mais complexas dentro das
# chaves das f-strings
a = 5
b = 3
mensagem = f"O resultado da soma de {a} e {b} é {a + b}."
print(mensagem)  # Saída: O resultado da soma de 5 e 3 é 8.

# Formatação Avançada:
# As f-strings também suportam formatação avançada, onde você pode especificar
# a largura do campo, a precisão e outros detalhes de formatação, semelhante ao
# método str.format()
numero = 12345
mensagem = f"Número: {numero:10d}"
print(mensagem)  # Saída: Número:      12345

preco = 19.99
mensagem = f"Preço: R$ {preco:6.2f}"
print(mensagem)  # Saída: Preço: R$  19.99

# Formatação básica de strings
# s - string
# d - int
# f - float
# .<número de dígitos>f
# x ou X - Hexadecimal
# (Caractere)(><^)(quantidade)
# > - Esquerda
# < - Direita
# ^ - Centro
# Sinal - +
# Ex.: 0>-100,.1f
# Conversion flags - !r !s !a
variavel = 'ABCD'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{1000.12458935654:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')
