# Herança Múltipla - Python Orietado a Objetos
# Quer dizer que no Python, uma classe pode estender várias outras classes.
#
# Herança Simples:
# Animal -> Mamífero -> Humano -> Pessoa -> Cliente
# Herança múltipla e mixins
# Log -> FileLog
# Animal -> Mamífero -> Humano -> Pessoa -> Cliente
# Cliente(Pessoa, FileLog)
#
# Python 3 usa C3 superclass linearization para gerar o método MRO
class A:
    ...

    def quem_sou(self):
        print('A')


class B(A):
    ...

    # def quem_sou(self):
    #     print('B')


class C(A):
    ...

    def quem_sou(self):
        print('C')


class D(B, C):
    ...

    # def quem_sou(self):
    #     print('D')


d = D()
d.quem_sou()
