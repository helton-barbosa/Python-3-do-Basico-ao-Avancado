# Relações entre classes: associação, agregação e composição
# Composição é uma especialização de agregação, onde a classe composta é
# responsável pela criação e destruição dos objetos que compõem a classe
# Quando o objeto pai for deletado, todas as referências dos objetos filhos
# também serão deletadas
class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []
    
    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))
    
    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)
    
    def __del__(self):
        print(f'Apagando, {self.nome}')


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero
    
    def __del__(self):
        print(f'Apagando, {self.rua}, {self.numero}')


cliente1 = Cliente('João')
cliente1.inserir_endereco('Rua A', 123)
cliente1.inserir_endereco('Rua B', 456)
cliente1.listar_enderecos()
del cliente1
