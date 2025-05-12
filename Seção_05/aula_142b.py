from abc import ABC, abstractmethod
import math


class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        ...

    @abstractmethod
    def calcular_perimetro(self):
        ...


class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * self.raio**2

    def calcular_perimetro(self):
        return 2 * math.pi * self.raio


class Quadrado(FormaGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado**2

    def calcular_perimetro(self):
        return 4 * self.lado


class Triangulo(FormaGeometrica):
    def __init__(self, base, altura, lado_1, lado_2, lado_3):
        self.base = base
        self.altura = altura
        self.lado_1 = lado_1
        self.lado_2 = lado_2
        self.lado_3 = lado_3

    def calcular_area(self):
        return 0.5 * self.base * self.altura

    def calcular_perimetro(self):
        return self.lado_1 + self.lado_2 + self.lado_3


circulo = Circulo(5)
print(f"Área do círculo: {circulo.calcular_area()}")
print(f"Perímetro do círculo: {circulo.calcular_perimetro()}")
print()
quadrado = Quadrado(4)
print(f"Área do quadrado: {quadrado.calcular_area()}")
print(f"Perímetro do quadrado: {quadrado.calcular_perimetro()}")
print()
triangulo = Triangulo(6, 8, 5, 5, 6)  # Exemplo de triangulo isósceles
print(f"Área do triângulo: {triangulo.calcular_area()}")
print(f"Perímetro do triângulo: {triangulo.calcular_perimetro()}")
