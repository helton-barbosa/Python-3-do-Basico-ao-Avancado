# print()
# É usado para imprimir
# print(*objects, sep='', end='\n', file=None, flush=None)
#
# *objects - Objetos que podem ser string, inteiro, ponto flutuante,
# variáveis e etc...
#
# sep='' - Separador que pode ser qualquer caractere ou None. Usado para
# separar os objetos na saída.
#
# end='' - Define o caractere que será exibido no fim da linha. Pode ser
# caracteres ou None.
# CRLF (Utilizado no Windows) - \r\n
# LF (Utilizado em Unix) - \n
#
# file=None - Redireciona a saída para um arquivo. Se não for especificado
# a saída é enviada para o console (sys.stdout)
#
# flush=False - O buffer de saída geralmente é determinado por arquivo.
# Se flush for True, a saída será enviada imediatamente.

print(12, 34, sep='-', end='\r\n') # Pula uma linha
print(56, 78, sep="-", end='\r\n\r\n') # Pula duas linhas
print('Fim')

