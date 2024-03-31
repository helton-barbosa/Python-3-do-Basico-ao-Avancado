# A interpolação de string com % em Python é uma técnica para formatar strings
# substituindo marcadores de posição % por valores específicos. Isso é feito
# usando o operador %, seguido por uma letra que indica o tipo de dado que será
# inserido na string. Aqui está uma explicação detalhada com exemplos:

# 1. Interpolação de Números Inteiros (%d):
# O marcador %d é usado para substituir números inteiros na string
idade = 25
mensagem = "Eu tenho %d anos." % idade
print(mensagem)  # Saída: Eu tenho 25 anos.

# 2. Interpolação de Números de Ponto Flutuante (%f):
# O marcador %f é usado para substituir números de ponto flutuante na string
altura = 1.75
mensagem = "Minha altura é %.2f metros." % altura
print(mensagem)  # Saída: Minha altura é 1.75 metros.

# 3. Interpolação de Strings (%s):
# O marcador %s é usado para substituir strings na string
nome = "Maria"
mensagem = "Meu nome é %s." % nome
print(mensagem)  # Saída: Meu nome é Maria.

# 4. Interpolação de Múltiplos Valores:
# Você pode usar múltiplos marcadores de posição na mesma string e fornecer
# múltiplos valores para substituição
nome = "João"
idade = 30
mensagem = "Olá, eu sou %s e tenho %d anos." % (nome, idade)
print(mensagem)  # Saída: Olá, eu sou João e tenho 30 anos.

# 5. Interpolação de Diferentes Tipos de Dados:
# Você pode combinar diferentes tipos de dados em uma única string usando os
# marcadores apropriados.
nome = "Ana"
idade = 25
altura = 1.65
mensagem = "%s tem %d anos e %.2f metros de altura." % (nome, idade, altura)
print(mensagem)  # Saída: Ana tem 25 anos e 1.65 metros de altura.

# 6. Ajustando a Largura do Campo e Precisão:
# Você pode ajustar a largura do campo e a precisão de valores numéricos usando
# um formato específico %Nd para números inteiros e %N.Mf para números de ponto
# flutuante, onde N é a largura do campo e M é o número de casas decimais.
numero = 12345
mensagem = "Número: %10d" % numero
print(mensagem)  # Saída: Número:      12345

preco = 19.99
mensagem = "Preço: R$ %6.2f" % preco
print(mensagem)  # Saída: Preço: R$  19.99

# Considerações Adicionais:
# %d, %f e %s são os marcadores de posição mais comuns para inteiros, floats e
# strings, respectivamente.
# %10d reserva um campo de 10 caracteres para o número inteiro.
# %6.2f reserva um campo de 6 caracteres com duas casas decimais para o número
# de ponto flutuante.
# A interpolação de string com % em Python é uma técnica poderosa e versátil
# para formatar strings de maneira dinâmica e controlada. É amplamente
# utilizada e oferece muitas opções para personalizar a formatação conforme
# necessário. Certifique-se de compreender bem como funciona e pratique sua
# utilização para se familiarizar com ela.
