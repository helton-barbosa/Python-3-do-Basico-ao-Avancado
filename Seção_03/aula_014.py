# O método format() em Python é uma maneira poderosa de formatar strings,
# permitindo a inserção de valores em posições específicas dentro de uma string
# formatada. Ele oferece uma maneira mais flexível e legível de criar strings
# formatadas em comparação com a interpolação de strings (usando %) e é
# altamente recomendado para novos desenvolvimentos.

# 1. Posicional:
# No método format(), você pode especificar os valores que deseja inserir na
# string formatada na ordem em que devem aparecer.
nome = 'Helton'
idade = 38
mensagem_01 = "Olá, meu nome é {} e tenho {} anos.".format(nome, idade)
print('1. Posicional:')
print(mensagem_01)

# 2. Por índice:
# Você também pode usar índices numéricos para especificar a ordem dos valores
# a serem inseridos na string formatada.
mensagem_02 = "Olá, tenho {1} anos e me chamo {0}".format(nome, idade)
print('\n2. Por índice:')
print(mensagem_02)

# 3. Nomeado:
# É possível nomear os campos de substituição e passar os valores
# correspondentes usando os nomes especificados.
mensagem_03 = "Minha cidade natal é {cidade}.".format(cidade="Aracaju")
print('\n3. Nomeado:')
print(mensagem_03)

# 4. Acessando elementos de listas ou dicionários:
# Você pode acessar elementos de listas ou dicionários diretamente usando
# índices ou chaves dentro das chaves de substituição.
dados_01 = ["Rose", 2, "Pará"]
dados_02 = {"nome": "João Victor", "idade": 13}
dados_03 = {"nome": "Rebecca", "idade": 12}
mensagem_04 = "{0[0]} é do {0[2]}. E temos {0[1]} filhos.".format(dados_01)
mensagem_04_a = "{dados_02[nome]} tem {dados_02[idade]} anos.".format(
    dados_02=dados_02
    )
mensagem_04_b = "{dados_03[nome]} tem {dados_03[idade]} anos.".format(
    dados_03=dados_03
    )
print('\n4. Acessando elementos de listas ou dicionários:')
print(mensagem_04)
print(mensagem_04_a)
print(mensagem_04_b)

# 5. Alinhamento e formatação:
# Você pode especificar o alinhamento, largura e precisão de um campo formatado
preco = 49.99
mensagem = "O preço é: R${:15.2f}".format(preco)
print('\n5. Alinhamento e formatação:')
print(mensagem)
