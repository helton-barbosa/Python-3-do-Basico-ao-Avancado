"""
Exercício
Exiba os índices da lista
0 Zinha <class 'str'>
1 Helton <class 'str'>
2 Rose <class 'str'>
3 JV <class 'str'>
4 Becca <class 'str'>
5 Maria Hilda <class 'str'>
6 Antônio <class 'str'>
"""
lista = ['Zinha', 'Helton', 'Rose', 'JV', 'Becca', 'Maria Hilda', 'Antônio']
lista.append('Nabucodonosor')


indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
