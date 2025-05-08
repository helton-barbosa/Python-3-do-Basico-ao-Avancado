# super() é a super classe na sub classe
# Classe principal (Pessoa)
# -> super class, base class, parent class
# Classes filhas (Cliente)
# -> sub class, derived class, child class
class MinhaString(str):
    def upper(self):
        return super().upper()

    def title(self):
        return super().title()


class PrimeiraClasse:
    atributo_a = 'Valor da primeira classe'

    def metodo(self):
        print(f'Primeira classe')


class SegundaClasse(PrimeiraClasse):
    atributo_b = 'Valor da segunda classe'

    def metodo(self):
        print(f'Segunda classe')


class TerceiraClasse(SegundaClasse):
    atributo_c = 'Valor da terceira classe'

    def metodo(self):
        super(SegundaClasse, self).metodo()
        print(f'Terceira classe')


nome = MinhaString('Helton Barbosa Santos')
print(nome)
print(f'upper -> {nome.upper()}')
print(f'lower -> {nome.lower()}')
print(f'capitalize -> {nome.capitalize()}')
print(f'title -> {nome.title()}')
print(f'split -> {nome.split()}')
print(f'--------------------------------------------')
terceira = TerceiraClasse()
print(terceira.atributo_a)
print(terceira.atributo_b)
print(terceira.atributo_c)
terceira.metodo()
