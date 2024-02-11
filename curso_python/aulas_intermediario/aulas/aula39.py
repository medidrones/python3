# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

import aula39_m
from aula39_m import soma, variavel_modulo

print('Este módulo se chama', __name__)
# print('Este módulo se chama', __name__)
print(aula39_m.variavel_modulo)
print(variavel_modulo)
print(soma(2, 3))
print(aula39_m.soma(2, 3))