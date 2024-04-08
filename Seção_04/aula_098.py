import importlib

import aula_098a

print(aula_098a.variavel)

for i in range(10):
    importlib.reload(aula_098a)
    print(i)

print('Fim')
