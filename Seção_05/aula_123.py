# Escopo da classe e de métodos da classe
# Uma variável de classe é uma variável que é compartilhada por todas as
# instâncias de uma classe. Uma variável de classe é inicializada
# automaticamente quando uma nova instância de uma classe é criada e usa o self
# Variáveis de classe são atribuídas dentro da definição de uma classe,
# mas fora de qualquer método da classe.
# Variáveis de classe não são usadas com tanta frequência quanto
# variáveis de instância.
class Animal:
    # nome = 'Jabuti'  # Atributo de classe

    def __init__(self, nome):
        self.nome = nome

    def comendo(self, alimento):
        return f'{self.nome} comendo {alimento}'

    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)


anfibio = Animal('Sapo')
print(anfibio.executar('moscas.'))
