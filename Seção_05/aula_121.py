# Métodos em instâncias de classes Python
# Hardcoded é algo que foi escrito diretamente no código fonte

class Carro:
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.ligado = False
        self.km = 0

    def acelerar(self):
        print(f'Acelerando o carro {self.modelo}...')


hb20 = Carro('HB20', 2025, 'Branca')
print(hb20.modelo)

hb20.acelerar()
