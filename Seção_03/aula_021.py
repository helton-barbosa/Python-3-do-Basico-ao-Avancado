# O operador lógico and em Python é usado para combinar duas expressões
# booleanas. Ele retorna True apenas se ambos os operandos forem True, caso
# contrário, retorna False. Aqui está uma explicação detalhada com exemplos:

# Exemplo Simples:
x = 5
print(x > 0 and x < 10)  # Saída: True
# Neste exemplo, a expressão x > 0 and x < 10 é avaliada como True porque x é
# maior que 0 e menor que 10.

# Utilizando em Condicional:
# Neste exemplo, a mensagem "Você é um adulto jovem." será impressa se a idade
# estiver entre 18 e 30 (inclusive). Caso contrário, a mensagem "Você não é um
# adulto jovem." será impressa.
idade = 25
if idade >= 18 and idade <= 30:
    print("Você é um adulto jovem.")
else:
    print("Você não é um adulto jovem.")

# Encadeamento de Condições:
# Neste exemplo, a mensagem "O valor é maior que 10 e é par." será impressa se
# o valor for maior que 10 e for par (ou seja, o resto da divisão por 2 é igual
# a 0).
valor = 15
if valor > 10 and valor % 2 == 0:
    print("O valor é maior que 10 e é par.")
else:
    print("O valor não satisfaz as condições.")

# Combinando com Expressões Complexas:
# Neste exemplo, a mensagem "Condições satisfeitas." será impressa se x for
# maior que 0 e y for menor que 10 e a soma de x e y for igual a 17.
x = 5
y = 12
if x > 0 and y < 10 and x + y == 17:
    print("Condições satisfeitas.")
else:
    print("Condições não satisfeitas.")

# O operador and é útil para combinar várias condições em uma única expressão
# lógica. Ele permite que você crie condições mais complexas que devem ser
# atendidas simultaneamente. Certifique-se de compreender bem como funciona e
# se-o conforme necessário para controlar o fluxo do seu programa de maneira
# eficaz.
