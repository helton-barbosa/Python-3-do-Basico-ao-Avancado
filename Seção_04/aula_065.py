"""
Introdução às funções (def) em Python Funções são trechos de código usados para
replicar determinada ação ao longo do seu código. Elas podem receber valores
para parâmetros (argumentos) e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""


def Print(a, b, c):
    print('Várias1')
    print('Várias2')
    print('Várias3')
    print('Várias4')


Print(1, 2, 3)


def imprimir(a, b, c):
    print(a, b, c)


imprimir('Helton', 'Barbosa', 'Santos Ferreira')
imprimir(4, 5, 6)


def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}!')


saudacao('Helton Barbosa')
saudacao('Rose Barbosa')
saudacao('João Victor')
saudacao('Rebecca')
saudacao()

