"""
    ATIVIDADE 05 - PRESENÇA: POO - P7 DE INFO - BEATRIZ V.

    ENUNCIADO: Determinar se 3 comprimentos podem formar um
    triângulo através de uma função que recebe 3 parâmetros
    e retorna um valor boolean
"""

i = 0
comprimentos = []

while i < 3:
    comprimentos.append(int(input(f'Digite o comprimento {i+1}: ')))
    i += 1


def verify_triangulo(lados):
    valido = False

    if lados[0] >= lados[1] + lados[2]:
        valido = False
    elif lados[1] >= lados[0] + lados[2]:
        valido = False
    elif lados[2] >= lados[0] + lados[1]:
        valido = False
    else:
        valido = True

    for x in lados:
        if x <= 0:
            valido = False

    return valido


if verify_triangulo(comprimentos):
    print('Seus comprimentos podem formar um triângulo')
else:
    print('Seus comprimentos não podem formar um triângulo')
