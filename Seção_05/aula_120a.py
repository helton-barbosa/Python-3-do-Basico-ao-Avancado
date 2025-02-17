class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade


p1 = Pessoa('Helton', 'Barbosa', 40)
p2 = Pessoa('Rose', 'Barbosa', 43)

print(f'Nome: {p1.nome}\nSobrenome: {p1.sobrenome}\nIdade: {p1.idade}')
print(f'Nome: {p2.nome}\nSobrenome: {p2.sobrenome}\nIdade: {p2.idade}')
