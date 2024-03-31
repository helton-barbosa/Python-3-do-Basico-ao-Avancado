# O operador lógico not em Python é usado para negar o valor de uma expressão
# booleana. Ele retorna True se a expressão for False e False se a expressão
# for True. Aqui está uma explicação detalhada com exemplos:

# Exemplo Simples:
x = 5
print(not x == 0)  # Saída: True
# Neste exemplo, a expressão x == 0 é False porque x não é igual a 0.
# O operador not nega esse resultado, portanto, a saída é True.

# Utilizando em Condicional:
idade = 25
if not idade < 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
# Neste exemplo, a condição idade < 18 é False porque a idade não é menor que
# 18. O operador not nega esse resultado, portanto, a mensagem "Você é maior de
# idade." será impressa.

# Combinando com Operadores Lógicos:
x = 5
y = 12
if not (x > 0 and y < 10):
    print("Pelo menos uma das condições não foi satisfeita.")
else:
    print("Ambas as condições foram satisfeitas.")
# Neste exemplo, a expressão (x > 0 and y < 10) é False porque x não é maior
# que 0 e y não é menor que 10. O operador not nega esse resultado, portanto,
# a mensagem "Pelo menos uma das condições não foi satisfeita." será impressa.

# Negando Valores Booleanos:
valor_verdadeiro = True
print(not valor_verdadeiro)  # Saída: False

valor_falso = False
print(not valor_falso)  # Saída: True
# Neste exemplo, o operador not nega os valores booleanos. Se o valor for True,
# ele será negado para False. Se o valor for False, ele será negado para True.

# O operador not é útil para inverter o valor de uma expressão booleana,
# o que pode ser útil em várias situações de programação. Certifique-se de
# compreender bem como funciona e use-o conforme necessário para controlar
# o fluxo do seu programa.
