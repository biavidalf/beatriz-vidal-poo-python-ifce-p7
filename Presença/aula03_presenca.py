"""
    ATIVIDADE 02 - PRESENÇA: POO - P7 DE INFO - BEATRIZ V.

    ENUNCIADO: Para ganhar o prêmio máximo na Mega Sena, é necessário
    acertar todos os 6 números em seu bilhete com os 6 números entre 1 e 60
    sorteados. Escreva um programa que gere uma seleção aleatória de 6 números para
    uma aposta. Certifique-se de que os 6 números selecionados não contenham
    duplicatas. Exibir os números em ordem crescente.
"""
from random import *

# Criando usando o type set porque já automaticamente elimina
# os números duplicados
numeros = set()


def gerar_numeros():
    while len(numeros) < 6:
        numeros.add(randint(1, 60))
    return numeros


gerar_numeros()
numeros_ordenados = sorted(numeros)

print(f'Os números gerados foram: {numeros_ordenados}')
