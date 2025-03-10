# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# @property é uma propriedade do objeto, ela é um método que se comporta como
# um atributo. Geralmente é usada nas seguintes situações:
# -> como getter
# -> para evitar quebrar código cliente
# -> para habilitar setter
# -> para executar ações ao obter um atributo
class Caneta:
    def __init__(self, cor):
        self.nova_cor = cor
        self.tampa = 'Preta'

    @property
    def cor(self):
        return self.nova_cor

    @property
    def cor_tampa(self, cor):
        return f'A cor da tampa é {self.tampa}'


caneta = Caneta('Prata')
print(caneta.cor)
print(caneta.tampa)
