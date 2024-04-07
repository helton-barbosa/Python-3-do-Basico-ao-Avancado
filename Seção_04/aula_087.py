# isinstace - para saber se objeto é de determinado tipo
lista_mista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]

for item in lista_mista:
    if isinstance(item, set):
        print('SET')
        item.add(5)
        print(f'{item} {isinstance(item, set)}\n')

    elif isinstance(item, str):
        print('STR')
        print(f'{item.upper()}\n')

    elif isinstance(item, (int, float)):
        print('NUM')
        print(f'{item}, {item * 2}\n')
    else:
        print('OUTRO')
        print(f'{item}\n')
