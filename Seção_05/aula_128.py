# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe
class Pessoa:
    ano = 2025

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def metodo_da_classe_1(self):
        print("Método da classe 1...")

    @classmethod
    def metodo_da_classe_2(cls):
        print("Método da classe 2...")

    @classmethod
    def criar_com_100_anos(cls, novo_nome):
        return f'{novo_nome} tem 100 anos.'


print(Pessoa.ano)  # Acessando o atributo da classe
p1 = Pessoa('Helton', 39)
# A linha abaixo vai dar erro
# Pessoa.metodo_da_classe_1()  # tentando acessar o metodo da classe sem o self
Pessoa.metodo_da_classe_1(p1)  # tentando acessar o metodo da classe com o self
p1.metodo_da_classe_1()  # Acessando o método da classe

Pessoa.metodo_da_classe_2()  # Acessando o método da classe sem o self

print(Pessoa.criar_com_100_anos("Rose"))
