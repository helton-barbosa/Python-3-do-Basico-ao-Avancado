# while é uma estrutura de controle de fluxo em Python que permite executar um
# bloco de código repetidamente enquanto uma condição especificada for
# verdadeira. break é uma palavra-chave que pode ser usada dentro de um loop
# para interromper sua execução, independentemente da condição de repetição.
# Aqui está uma explicação detalhada com exemplos:

# Usando while:
# A sintaxe básica do while é:
# while condicao:
# Bloco de código a ser executado enquanto a condição for verdadeira

contador = 0
while contador < 5:
    print(contador)
    contador += 1

# Neste exemplo, o bloco de código dentro do while será repetido enquanto o
# contador for menor que 5. Ele imprimirá os números de 0 a 4.

# Usando break:
# A palavra-chave break pode ser usada para interromper a execução de um loop
# antes que a condição de repetição se torne falsa.

# Exemplo:
contador = 0
while True:
    print(contador)
    contador += 1
    if contador >= 5:
        break

# Neste exemplo, o loop while será executado indefinidamente. No entanto,
# a execução será interrompida quando o contador atingir o valor de 5 devido
# ao uso do break.

# Utilizando while e break juntos:
# while e break são frequentemente usados juntos para criar loops com condições
# de saída personalizadas.

# Exemplo:
contador = 0
while True:
    print(contador)
    contador += 1
    if contador >= 5:
        break

# Neste exemplo, o loop while True cria um loop infinito. No entanto, o break é
# usado para sair do loop quando o contador atinge 5.
