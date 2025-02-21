# Escopo da classe e de métodos da classe
class Animal:
    # nome = 'Guaxinim'
    def __init__(self, nome):
        self.nome = nome

        variavel = 'valor'
        print(variavel)

    def comendo(self, alimento):
        return f'{self.nome} está comendo uma {alimento}'

    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)


exemplo = Animal(nome='Tartaruga')
print(exemplo.nome)
print(exemplo.executar('goiaba'))
