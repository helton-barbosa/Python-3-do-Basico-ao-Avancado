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
frutas = ['maçã', 'ata', 'laranja', 'limão', 'caqui', 'cajá']
verduras = ['jiló', 'ata', 'cebola', 'couve', 'jiló', 'ata']
frutas[1] = 'abacate'


print(f"Lista de frutas: {frutas}")

# Adicionando e Removendo Elementos:
# Exemplo:

# - append(): Adiciona um elemento ao final da lista.
frutas.append('morango')
print(f"append: {frutas}")

# - insert(): Insere um elemento em uma posição específica.
frutas.insert(1, 'caju')
print(f"insert: {frutas}")

# - remove(): Remove o primeiro elemento com o valor especificado.
frutas.remove('cajá')
print(f"remove: {frutas}")

# - pop(): Remove e retorna o elemento em uma posição específica.
frutas.pop(0)
print(f"pop: {frutas}")

# - index(): Retorna o índice da primeira ocorrência de um valor
print(f"index do elemento 'laranja': {frutas.index("laranja")}")


# - del: Remove um elemento de uma lista ou toda a lista.
del frutas[3]
print(f"del: {frutas}")

# - extend(): É usado para adicionar todos os elementos de uma lista ao final
# de outra lista.
frutas.extend(verduras)
print(f"extend: {frutas}")

# - +: É usado para concatenar duas listas, ou seja, criar uma nova lista
# contendo os elementos das duas listas
alimento = frutas + verduras
print(f"+: {alimento}")

# - count(): Retorna o número de ocorrências de um valor da lista
print(f"Quantidade de vezes de 'ata': {alimento.count("ata")}")

# - sort(): Ordena a lista
alimento.sort()
print(f"Ordem crescente: {alimento}")

# - reverse(): Ordem reversa da lista
alimento.reverse()
print(f"Ordem decrescente: {alimento}")

# - clear(): É usado para remover todos os elementos de uma lista.
alimento.clear()
print(f"clear: {alimento}")

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
