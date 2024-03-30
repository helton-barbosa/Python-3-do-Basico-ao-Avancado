# Variáveis são usadas para salvar algo na memória do computador
# PEP8: iniocie variáveis com letras minúsculas, pode usar
# números e underline _.
# O sinal de = é o operador de atribuição. Ele é usado para atribuir um valor
# a um nome (variável).
# Obs.: variáveis não são usadas pra abreviar código!
# Uso: nome_variavel = expressao

nome_completo = 'Helton Ferreira'
print(nome_completo)
soma_dois_mais_dois = 2 + 2
print(soma_dois_mais_dois)

nome = 'Rebecca'
idade = 12
auxiliar = idade >= 18
if auxiliar == True:
    maior_de_idade = 'é maior de idade'
else:
    maior_de_idade = 'não é maior de idade'

print(f'{nome} tem {idade} anos e {maior_de_idade}.')

