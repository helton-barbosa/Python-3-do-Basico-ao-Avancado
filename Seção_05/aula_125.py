# Atributos de uma Classe
class Pessoa:
    ano_atual = 2025

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.ano_atual = 2025

# Instanciando a Classedef get_ano_nascimento(self):
    def get_ano_nascimento(self):
        return self.ano_atual - self.idade


p1 = Pessoa('Helton', 40)
p2 = Pessoa('Rose', 43)
print(f'Ano atual: {Pessoa.ano_atual}')
Pessoa.ano_atual = 2030
print(f'Ano atual: {Pessoa.ano_atual}')
print(f'Ano atual: {p1.ano_atual}')
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
