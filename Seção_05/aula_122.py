# Entendendo self em classes Python
# Classe - Molde (geralmente sem dados)
# Instância da class (objeto) - Tem os dados
# Uma classe pode gerar várias instâncias
# O Classe o self é a própria instância da classe
class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} acelerando...')


fusca = Carro('Fusca')
fusca.acelerar()
print(fusca.nome)

celta = Carro('Celta')
celta.acelerar()
print(celta.nome)
