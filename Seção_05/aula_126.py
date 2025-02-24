# __dict__ e vars para atributos de instância
class Pessoa:
    ano_atual = 2025

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


dados = {'nome': 'José', 'idade': 60}
p1 = Pessoa('Helton', 40)
# p1.nome = 'Rose'
# print(p1.nome)
p1.__dict__['raca'] = 'preta'
print(p1.__dict__)
print(vars(p1))
pai = Pessoa(**dados)
print(pai.__dict__)
