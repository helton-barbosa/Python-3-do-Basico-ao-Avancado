# Relações entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada da associação entre dois ou mais
# objetos. Cada objeto terá seu próprio ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um objeto tem um ou muitos
# objetos. Os objetos podem viver separadamente, mas pode se tratar de uma
# relação onde um objeto precisa de outro para fazer determinada tarefa.
class Carrinho:
    def __init__(self):
        self._produtos = []

    def total(self):
        return sum([p.preco for p in self._produtos])

    def inserir_produtos(self, *produtos):
        # for produto in produtos:
           #  self._produtos.append(produto)

        # self._produtos.extend(produtos)

        self._produtos += produtos

    def listar_produtos(self):
        for produto in self._produtos:
            print(f'Produto: {produto.nome}\nPreço: R$ {produto.preco}')


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho = Carrinho()
prod_1, prod_2 = Produto('Caneta', 5.00), Produto('Caderno', 15.00)
carrinho.inserir_produtos(prod_1, prod_2)
carrinho.listar_produtos()
print(f'Valor total dos produtos é R$ {carrinho.total()}')

