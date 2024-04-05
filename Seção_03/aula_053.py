"""
enumerate - enumera iteráveis (índices)
"""
# [(0, 'Flamengo'), (1, 'Fluminense'), (2, 'Vasco da Gama'), (3, 'Botafogo')]
lista = ['Flamengo', 'Fluminense', 'Vasco da Gama']
lista.append('Botafogo')

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])

print()
for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)

print()
for tupla_enumerada in enumerate(lista):
    print('FOR da tupla:')
    for valor in tupla_enumerada:
        print(f'\t{valor}')
