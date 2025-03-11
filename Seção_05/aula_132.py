# @property + @setter são getter e setter no modo Pythônico
# - como getter
# - para evitar quebrar código cliente
# - para habilitar setter
# - para executar ações ao obter um atributo
# Atributos que começam com um ou dois underlines não devem ser usados fora da
# classe
class Caneta:
    def __init__(self, cor):
        # private ou protected
        self._cor = cor

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, valor):
        self._cor = valor


caneta = Caneta('Azul')
# getter -> obter valor
print(caneta.cor)
# setter -> altera valor
caneta.cor = 'Vermelha'
print(caneta.cor)
