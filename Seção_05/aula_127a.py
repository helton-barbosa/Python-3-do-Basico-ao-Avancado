# Exercício - Salve sua classe em json
# Salve os dados da sua classe em json
# e depois crie novamente as instâncias
# da classe com os dados salvos

import json

ARQUIVO = 'aula_127.json'


class Pessoa:
    def __init__(self, nome, idade, cor):
        self.nome = nome
        self.idade = idade
        self.cor = cor


p1 = Pessoa('Helton', 40, 'preta')
p2 = Pessoa('Rose', 43, 'parda')
p3 = Pessoa('José', 60, 'branca')

bd = [vars(p1), vars(p2), vars(p3)]


def fazer_dump():
    with open(ARQUIVO, 'w') as arquivo:
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    fazer_dump()
