# Herança simples - Relação entre classes
# Associação usa
# Agregação tem
# Composição é dono de
# Herança é um
#
# Herança ou Composição
#
# Classe principal (Pessoa)
# -> super class, base class, parent class
# Classes filhas (Cliente)
# -> sub class, derived class, child class
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def nome_classe(self):
        print('Classe Pessoa')
        return f'{self.nome} da classe "{self.__class__.__name__}"'


class Aluno(Pessoa):
    def nome_classe(self):
        print('Classe Aluno')
        return f'{self.nome} da classe "{self.__class__.__name__}"'


class Cliente(Pessoa):
    def nome_classe(self):
        print('Classe Cliente')
        return f'{self.nome} da classe "{self.__class__.__name__}"'


aluno_1 = Aluno('João', 'da Silva e Santos')
cliente_1 = Cliente('Maria', 'da Silva e Santos')

print(cliente_1.nome_classe())
print(cliente_1.nome, cliente_1.sobrenome)
print()
print(aluno_1.nome_classe())
print(aluno_1.nome, aluno_1.sobrenome)

# help(Cliente)
