import json
from aula_127a import ARQUIVO, Pessoa

with open(ARQUIVO, 'r') as arquivo:
    pessoas = json.load(arquivo)
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])

    print(f'Nome: {p1.nome}, Idade: {p1.idade}')
    print(f'Nome: {p2.nome}, Idade: {p2.idade}')
    print(f'Nome: {p3.nome}, Idade: {p3.idade}')
