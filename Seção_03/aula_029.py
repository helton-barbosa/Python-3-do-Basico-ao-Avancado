# Introdução ao try/except
# try -> tentar executar o código
# except - ocorreu algum erro ao tentar executar

numero_str = input('Vou dobrar o número que você digitar: ')

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número')

# essa não é a forma correta de usar o try/except, mas deixarei assim
try:
    print(f'STR: {numero_str}')
    numero_float = float(numero_str)
    print(f'FLOAT: {numero_float}')
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')
