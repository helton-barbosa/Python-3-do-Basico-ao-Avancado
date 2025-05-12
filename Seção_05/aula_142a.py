from abc import ABC, abstractmethod


class Robo(ABC):  # Manual de instruções (Classe Abstrata)
    @abstractmethod
    def criar_cabeca(self):
        ...  # Não implementa aqui, as classes concretas a implementam

    @abstractmethod
    def criar_corpo(self):
        ...  # Não implementa aqui, as classes concretas a implementam

    @abstractmethod
    def criar_pernas(self):
        ...  # Não implementa aqui, as classes concretas a implementam


class RoboCombate(Robo):  # Robô de Combate (Classe CXoncreta)
    def criar_cabeca(self):
        print("Criando cabeça com visor de combate")

    def criar_corpo(self):
        print("Criando corpo com placas de armadura")

    def criar_pernas(self):
        print("Criar pernas robustas")


class RoboCorrida(Robo):  # Robô de Corrida (Classe Concreta)
    def criar_cabeca(self):
        print("Criando cabeça aerodimâmica com sensor de velocidade")

    def criar_corpo(self):
        print("Criando corpo baixo e largo")

    def criar_pernas(self):
        print("Criando pernas com rodas grandes")


robo1 = RoboCorrida()
robo1.criar_cabeca()
robo1.criar_corpo()
robo1.criar_pernas()
print()
robo2 = RoboCombate()
robo2.criar_cabeca()
robo2.criar_corpo()
robo2.criar_pernas()
