# A estrutura de controle while em Python é usada para executar um bloco de
# código repetidamente enquanto uma condição específica for verdadeira.
# O comando continue é usado dentro de um loop para pular a iteração atual e
# continuar com a próxima iteração do loop. Aqui está uma explicação detalhada
# com exemplos:

# Usando continue:
# O comando continue é usado dentro de um loop para pular a iteração atual e
# continuar com a próxima iteração do loop.

# Exemplo:
contador = 0
while contador < 5:
    contador += 1
    if contador == 3:
        continue  # pula a iteração quando contador é igual a 3
    print(contador)

# Neste exemplo, o loop while imprimirá os números de 1 a 5, pulando a
# impressão do número 3 devido ao uso do continue.

# Utilizando while e continue juntos:
# while e continue são frequentemente usados juntos para criar loops com
# comportamentos específicos.

# Exemplo:
contador = 0
while contador < 5:
    contador += 1
    if contador % 2 == 0:
        continue  # pula a iteração se o contador for par
    print(contador)

# Neste exemplo, o loop while imprimirá apenas os números ímpares de 1 a 5,
# pulando a impressão dos números pares devido ao uso do continue.
