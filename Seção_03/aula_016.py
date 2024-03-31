# As estruturas condicionais em Python (if / elif / else) são usadas para
# executar diferentes blocos de código com base em condições específicas.
# Elas permitem que o programa tome decisões e execute diferentes ações
# com base em avaliações booleanas. Aqui está uma explicação detalhada
# com exemplos:

# 1. Declaração if simples:
# A declaração if verifica se uma condição é verdadeira e executa um bloco de
# código se a condição for verdadeira.
print('\n1. Declaração if simples:')
idade = 18
if idade >= 18:
    print("Você é maior de idade.")

# 2. Declaração if com else:
# A declaração else é usada para executar um bloco de código quando a condição
# do if não é verdadeira.
print('\n2. Declaração if com else:')
idade = 15
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# 3. Declaração if com elif:
# A declaração elif permite verificar múltiplas condições, executando o bloco
# de código associado à primeira condição verdadeira encontrada.
print('\n3. Declaração if com elif:')
nota = 75
if nota >= 90:
    print("Aprovado com distinção.")
elif nota >= 60:
    print("Aprovado.")
else:
    print("Reprovado.")

# 4. Aninhamento de declarações condicionais:
# Você pode aninhar declarações condicionais dentro de outras declarações
# condicionais para lidar com casos mais complexos.
print('\n4. Aninhamento de declarações condicionais:')
idade = 18
if idade >= 18:
    if idade == 18:
        print("Você acabou de atingir a maioridade.")
    else:
        print("Você é maior de idade há algum tempo.")
else:
    print("Você é menor de idade.")

# 5. Operadores lógicos:
# Você pode usar operadores lógicos como and, or e not para combinar condições
# em declarações condicionais.
print('\n5. Operadores lógicos:')
idade = 17
sexo = "Feminino"
if idade >= 18 and sexo == "Feminino":
    print("Você é uma mulher maior de idade.")
else:
    print("Você não é uma mulher maior de idade.")

# As estruturas condicionais são fundamentais em Python para controle de fluxo
# e tomada de decisões dentro do programa. Elas permitem que você crie progs
# mais dinâmicos e adapte o comportamento do programa com base em diferentes
# situações. Certifique-se de entender bem como funcionam e pratique escrevendo
# diferentes tipos de condições para se familiarizar com elas.
