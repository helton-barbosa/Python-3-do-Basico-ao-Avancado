# Em Python, id é uma função embutida que retorna o identificador único de um
# objeto. Cada objeto em Python tem um identificador único, que é atribuído a
# ele quando é criado e nunca muda durante o ciclo de vida desse objeto.
# O identificador é geralmente implementado como o endereço de memória do
# objeto, embora isso possa variar dependendo da implementação específica do
# interpretador Python. Aqui está uma explicação detalhada com exemplos:

# Obtendo o ID de um Objeto:
# Para obter o ID de um objeto em Python, você simplesmente chama a função id
# passando o objeto como argumento.

# Exemplo:
x = 42
print('\nObtendo o ID de um Objeto:')
print(id(x))  # (um número único que identifica o objeto inteiro)

# Identificadores Únicos:
# O identificador único de um objeto é garantido ser único durante toda a
# execução do programa. Dois objetos diferentes nunca terão o mesmo ID, a menos
# que sejam o mesmo objeto.

# Exemplo:
x = 42
y = 42
print('\nIdentificadores Únicos:')
print(id(x))
print(id(y))  # (mesmo ID, pois ambos apontam para o mesmo objeto inteiro)

# Identidade de Objetos:
# A identidade de um objeto em Python é sua característica de ser único.
# Dois objetos são considerados idênticos se tiverem o mesmo ID.

# Exemplo:
x = [1, 2, 3]
y = [1, 2, 3]
print('\nIdentidade de Objetos:')
print(id(x))  # Saída: ID do objeto x
print(id(y))  # Saída: ID do objeto y (diferente de x)
print(x is y)  # Saída: False (objetos diferentes, apesar de valores iguais)

# Utilização em Estruturas de Dados:
# O ID de um objeto é frequentemente utilizado em algoritmos que requerem
# identificação única de objetos ou em estruturas de dados personalizadas.


# Exemplo:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(1)
node2 = Node(2)

# Armazenando referências dos nós em um dicionário usando seus IDs como chaves
node_map = {id(node1): node1, id(node2): node2}

# Recuperando um nó usando seu ID
node = node_map.get(id(node1))
print('\nUtilização em Estruturas de Dados:')
print(node.data)  # Saída: 1

# Embora os IDs de objetos sejam úteis em muitos cenários, é importante notar
# que eles não devem ser confundidos com igualdade de objetos. Dois objetos
# podem ter o mesmo valor, mas serem objetos diferentes com IDs diferentes.
# Portanto, ao comparar objetos, use o operador == para verificar igualdade de
# valores e o operador is para verificar identidade de objetos.
