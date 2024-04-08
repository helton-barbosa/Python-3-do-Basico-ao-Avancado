# nos caminhos de sys.path

import aula_097_1a
from aula_097_1a import soma, variavel_modulo

print('Este módulo se chama', __name__)
# print('Este módulo se chama', __name__)
print(aula_097_1a.variavel_modulo)
print(variavel_modulo)
print(soma(2, 3))
print(aula_097_1a.soma(2, 3))
