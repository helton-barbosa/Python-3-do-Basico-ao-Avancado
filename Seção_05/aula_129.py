# @staticmethod (método estático) são métodos que estão dentro de uma classe,
# mas não tem acesso ao self nem ao cls. De forma resumida, são funções que
# existem dentro da classe apenas para organização de código.
class Classe:
    @staticmethod
    def funcao_na_classe_sem_argumentos():
        print('Sem argumentos')

    @staticmethod
    def funcao_na_classe_com_argumentos(*args, **kwargs):
        print(f'Com argumentos: {args}, {kwargs}')


c1 = Classe()
c1.funcao_na_classe_sem_argumentos()
Classe.funcao_na_classe_sem_argumentos()

c2 = Classe()
c2.funcao_na_classe_com_argumentos(1, 2, 3, 4, 5, nome='Helton', idade=39)
Classe.funcao_na_classe_com_argumentos(1, 2, 3, 4, 5, nome='Rose', idade=42)
