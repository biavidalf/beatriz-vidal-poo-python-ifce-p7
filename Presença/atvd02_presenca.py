"""
    ATIVIDADE 02 - PRESENÇA: POO - P7 DE INFO - BEATRIZ V.
"""
RED = "\033[1;31m"
RESET = "\033[0;0m"


# Funções
def sujar_louca(pilha, louca):
    pilha.append(louca)
    print(f'Mais um {louca.lower()} sujo')


def limpar_louca(pilha):
    pilha.pop()
    print('Uma louça lavada')


def mais_uma_pessoa(fila, nome):
    fila.append(nome.title())
    print(f'{nome.title()} foi adicionado na fila')


def pessoa_atendida(fila):
    del(fila[0])
    print('Primeiro da fila atendido com sucesso')


def adicionar_tarefa(lista, tarefa, local):
    lista.insert(local, tarefa)
    print(f'A tarefa {lista_afazeres[local].lower()} foi adicionada no índice {local}')


def remover_tarefa(lista, local):
    del(lista[local])
    print(f'A tarefa {lista_afazeres[local].lower()} foi realizada')


# Parte 1 - PILHAS
print(RED + 'EXERCÍCIO 01:\n' + RESET)
pilha_louca = []
sujar_louca(pilha_louca, 'Prato')
sujar_louca(pilha_louca, 'Copo')
sujar_louca(pilha_louca, 'Garfo')
print(pilha_louca)
limpar_louca(pilha_louca)
print(pilha_louca)
sujar_louca(pilha_louca, 'Garfo')
print(pilha_louca)
limpar_louca(pilha_louca)
print(pilha_louca)

# Parte 2 - FILAS
print(RED + '\nEXERCÍCIO 02:\n' + RESET)
fila_loja = []
mais_uma_pessoa(fila_loja, 'beatriz')
mais_uma_pessoa(fila_loja, 'layla')
mais_uma_pessoa(fila_loja, 'Jorge')
mais_uma_pessoa(fila_loja, 'henrique')
print('Pessoas restantes: ', fila_loja)
pessoa_atendida(fila_loja)
print('Pessoas restantes: ', fila_loja)

# Parte 3 - LISTA ENCADEADA
print(RED + '\nEXERCÍCIO 03:\n' + RESET)
lista_afazeres = []
adicionar_tarefa(lista_afazeres, 'Varrer a casa', 0)
adicionar_tarefa(lista_afazeres, 'Estudar', 1)
adicionar_tarefa(lista_afazeres, 'Ir no mercado', 2)
print()
remover_tarefa(lista_afazeres, 1)
print()
for x in lista_afazeres:
    print(f'{lista_afazeres.index(x)}: {x}')
print()
adicionar_tarefa(lista_afazeres, 'Lavar a louça', 0)
print()
for x in lista_afazeres:
    print(f'{lista_afazeres.index(x)}: {x}')
