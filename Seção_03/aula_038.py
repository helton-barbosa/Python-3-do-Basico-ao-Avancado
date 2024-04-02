# Quando você usa um while dentro de outro while, você está aninhando loops.
# Isso significa que um loop está dentro do outro. Isso é comumente usado
# quando você precisa repetir uma ação em uma série de itens, e cada item
# também precisa ser processado repetidamente. Aqui está uma explicação
# detalhada com exemplos:

# Exemplo de while dentro de while:
# Exemplo de um loop while dentro de outro
linha = 1
while linha <= 3:  # Loop externo para imprimir linhas
    coluna = 1
    while coluna <= 3:  # Loop interno para imprimir colunas
        print(f'({linha}, {coluna})', end=' ')
        coluna += 1
    print()  # Imprime uma nova linha após cada linha de colunas
    linha += 1


# O primeiro while é responsável por iterar sobre as linhas.
# O segundo while é responsável por iterar sobre as colunas em cada linha.
# Dentro do loop externo, o loop interno é executado várias vezes para imprimir
# as colunas para cada linha.
# Depois que todas as colunas para uma linha são impressas, uma nova linha é
# impressa usando print().
