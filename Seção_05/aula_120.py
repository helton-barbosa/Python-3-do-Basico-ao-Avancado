# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que podem
# ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de classes

class Pessoa:
    ...


p1 = Pessoa()
p1.nome = "Helton"
p1.idade = 40
print(p1)
print(p1.nome)
print(p1.idade)
print(f'p1 - {type(p1)}')
print(f'Pessoa - {type(Pessoa)}')
print(p1.__class__.__name__)
print(p1.__dict__)
