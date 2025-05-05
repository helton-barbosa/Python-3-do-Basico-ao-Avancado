# Exercício com classes
# 1 - Crie uma classe Carro com atributo nome
# 2 - Crie uma classe Motor com atributo nome
# 3 - Crie uma classe Fabricante com atributo nome
# 4 - Faça a ligação entre Carro e um Motor
# Obs.: Um motor pode ter vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode ter vários carros
# Exiba o nome do carro, motor e fabricante na tela
class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
        self._tipo = None
    
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor
    
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor
    
    @property
    def tipo(self):
        return self._tipo
    
    @tipo.setter
    def tipo(self, valor):
        self._tipo = valor


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


class Tipo:
    def __init__(self, nome):
        self.nome = nome


hb = Carro('HB20')
volkswagen = Fabricante('Hyundai')
moto_1_0 = Motor('Turbo TGDI')
tipo = Tipo('Safaty')

hb.fabricante = volkswagen
hb.motor = moto_1_0
hb.tipo = tipo

print(f'Carro: {hb.nome}')
print(f'Fabricante: {hb.fabricante.nome}')
print(f'Motor: {hb.motor.nome}')
print(f'Tipo: {hb.tipo.nome}')
