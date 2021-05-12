"""
    ATIVIDADE 03 - PRESENÇA: POO - P7 DE INFO - BEATRIZ V.

    ENUNCIADO: O triângulo pode ser classificado com base no comprimento de
    seus lados em equilátero, isósceles ou escaleno. Todos os três lados de um
    triângulo equilátero têm o mesmo comprimento. Um triângulo isósceles tem dois
    lados que são do mesmo comprimento e um terceiro lado que é diferente comprimento.
    Se todos os lados tiverem comprimentos diferentes, o triângulo é escaleno.
    Escreva um programa que leia os comprimentos dos três lados de um triângulo do usuário.
    Em seguida, exiba uma mensagem que declara o tipo do triângulo.
"""
# Criar um contador para armazenar os 3 lados dos triângulos
i = 0
lados = []

while i < 3:
    lados.append(input(f'Digite o lado {i+1}: '))
    i += 1

tipo = ''

if lados[0] == lados[1] and lados[1] == lados[2]:
    tipo = 'equilátero'
elif lados[0] != lados[1] and lados[1] != lados[2]:
    tipo = 'escaleno'
else:
    tipo = 'isósceles'

print(f'O tipo do triângulo é: {tipo}')
