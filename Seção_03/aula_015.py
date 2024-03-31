# A função input() em Python é usada para receber entrada do usuário através do
# teclado. Ela espera que o usuário insira algum valor e pressione a tecla
# Enter. O valor inserido é tratado como uma string e pode ser armazenado em
# uma variável para uso posterior.

# Exemplo Básico:
nome = input("Digite seu nome: ")
print(f"Olá, {nome}")

# Convertendo para Outros Tipos de Dados:
idade = int(input("Digite sua idade: "))
ano_nascimento = 2024 - idade
print(f"Você nasceu em, {ano_nascimento}")

# Usando input() em Expressões:
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
soma = numero1 + numero2
print("A soma é:", soma)

# Limitando o Número de Caracteres:
senha = input("Digite sua senha (máx. 8 caracteres): ")[:8]
print(f"Sua senha é: {senha}")
