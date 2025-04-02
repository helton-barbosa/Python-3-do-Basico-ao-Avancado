# Encapsulamento (modificadores de acesso: publuic, private e protected)
# Python não tem modificadores de acesso
# Mas podemos seguir as seguintes convenções:
#  (sem underline) = public (público)
#       pode ser usado em qualquer lugar
# _ (um underline) = protected (protegido)
#       não deve ser usado fora da classe ou de subclasses
# __ (dois underlines) = private (privado)
#       "name mangling" (desfiguração de nomes) em Python
#       só deve ser usado na classse em que foi declarado.
class Foo:
    def __init__(self):
        self.public = 'Isso é público'
        self._protected = 'Isso é protegido'
        self.__private = 'Isso é privado'

    def metodo_publico(self):
        return 'Isso é um método público'

    def _metodo_protegido(self):
        return 'Isso é um método protegido'

    def __metodo_privado(self):
        return 'Isso é um método privado'


f = Foo()
print(f.public)  # Isso é público
print(f._protected)  # Isso é protegido
# print(f.__private)  # Isso é privado
print(f._Foo__private)  # Isso é privado
print(f.metodo_publico())  # Isso é público também
print(f._metodo_protegido())  # Isso é protegido também
# print(f.__metodo_privado())  # Isso é privado também
print(f._Foo__metodo_privado())  # Isso é privado também
