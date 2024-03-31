# O operador lógico or em Python é usado para combinar duas expressões
# booleanas. Ele retorna True se pelo menos um dos operandos for True,
# caso contrário, retorna False. Aqui está uma explicação detalhada com
# exemplos:

# Exemplo Simples:
x = 5
print(x < 0 or x > 10)  # Saída: False
# Neste exemplo, a expressão x < 0 or x > 10 é avaliada como False porque x não
# é menor que 0 e também não é maior que 10.

# Utilizando em Condicional:
idade = 25
if idade < 18 or idade > 60:
    print("Você não está na faixa etária de trabalho.")
else:
    print("Você está na faixa etária de trabalho.")
# Neste exemplo, a mensagem "Você não está na faixa etária de trabalho." será
# impressa se a idade for menor que 18 ou maior que 60. Caso contrário, a
# mensagem "Você está na faixa etária de trabalho." será impressa.

# Encadeamento de Condições:
valor = 15
if valor < 10 or valor % 2 == 0:
    print("O valor é menor que 10 ou é par.")
else:
    print("O valor não satisfaz as condições.")
# Neste exemplo, a mensagem "O valor é menor que 10 ou é par." será impressa se
# o valor for menor que 10 ou for par (ou seja, o resto da divisão por 2 
# igual a 0).

# Combinando com Expressões Complexas:
x = 5
y = 12
if x > 0 or y < 10 or x + y == 17:
    print("Pelo menos uma das condições foi satisfeita.")
else:
    print("Nenhuma das condições foi satisfeita.")
# Neste exemplo, a mensagem "Pelo menos uma das condições foi satisfeita." será
# impressa se x for maior que 0 ou y for menor que 10 ou a soma de x e y for
# igual a 17.

# O operador or é útil para criar condições em que pelo menos uma das
# expressões deve ser verdadeira. Ele permite que você crie expressões lógicas
# mais complexas e versáteis em seus programas Python. Certifique-se de
# compreender bem como funciona e use-o conforme necessário para controlar o
# fluxo do seu programa.
