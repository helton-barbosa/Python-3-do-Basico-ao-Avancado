"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Helton', 'Rose', 1, True, 1.2]
lista_b = lista_a.copy()
# copy() retorna uma nova lista com os mesmos valores
lista_b = lista_b
# As duas variáveis estão apontando para o mesmo endereço da memória

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)
