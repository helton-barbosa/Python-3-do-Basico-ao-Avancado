# dir, hasattr e getattr em Python
string = 'Paralelepipedo'
metodo = 'capitalize'

if hasattr(string, metodo):
    print(f'Existe {metodo}')
    print(getattr(string, metodo)())
else:
    print(f'Não existe o método {metodo}')

print(dir(string))
