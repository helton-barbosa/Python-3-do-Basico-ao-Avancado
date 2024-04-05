# Em Python, uma lista é um tipo de dados que pode armazenar uma coleção
# ordenada de elementos. É uma estrutura de dados mutável, o que significa que
# você pode modificar, adicionar e remover elementos conforme necessário.
# Aqui está uma explicação detalhada sobre listas com exemplos:

# Criando uma Lista:
# Uma lista é definida usando colchetes [], e os elementos são separados por
# vírgulas.

# Exemplo:
numeros = [1, 2, 3, 4, 5]  # Criando uma lista de números inteiros
frutas = ['maçã', 'banana', 'laranja']  # Criando uma lista de strings
misturado = [10, 'abc', True, 3.14]  # Criando uma lista mista

# Modificando Elementos:
# Você pode modificar os elementos de uma lista atribuindo um novo valor a um
# índice específico.

# Exemplo:
frutas = ['maçã', 'banana', 'laranja', 'tamarindo', 'pitanga', 'maracujá']
verduras = ['abóbora', 'batata', 'beterraba']
frutas[1] = 'abacate'
print(frutas)

# Adicionando e Removendo Elementos:
# - append(): Adiciona um elemento ao final da lista.
# - insert(): Insere um elemento em uma posição específica.
# - remove(): Remove o primeiro elemento com o valor especificado.
# - pop(): Remove e retorna o elemento em uma posição específica.
# - del: Remove um elemento de uma lista ou toda a lista.
# - extend(): É usado para adicionar todos os elementos de uma lista ao final
# de outra lista.
# - +: É usado para concatenar duas listas, ou seja, criar uma nova lista
# contendo os elementos das duas listas
# - clear(): É usado para remover todos os elementos de uma lista.
# Exemplo:
frutas.append('morango')
print(frutas)

frutas.insert(1, 'abacate')
print(frutas)

frutas.remove('maracujá')
print(frutas)

frutas.pop(0)
print(frutas)

del frutas[3]
print(frutas)

frutas.extend(verduras)
print(frutas)

alimento = frutas + verduras
print(alimento)

alimento.clear()
print(alimento)

"""
Notas adicionais:
Listas podem conter elementos de diferentes tipos de dados, incluindo outras
listas (listas aninhadas).
Os elementos de uma lista podem ser acessados, modificados e removidos usando
índices. As listas são mutáveis, o que significa que você pode modificar seus
elementos após a criação.
As listas são uma estrutura de dados flexível e amplamente utilizada em Python
devido à sua versatilidade e facilidade de uso.
"""
