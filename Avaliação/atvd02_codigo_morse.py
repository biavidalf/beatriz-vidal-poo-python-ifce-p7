"""
    AVALIAÇÃO 02(POO) - TRADUTOR CÓDIGO MORSE
    BEATRIZ VIDAL FREIRE - P7 DE INFORMÁTICA, IFCE CAMPUS FORTALEZA
"""
# Implementei cores para destacar os caracteres permitidos
# Reset p/ voltar para a cor normal, senão o resto ficaria vermelho
RED = "\033[1;31m"
RESET = "\033[0;0m"

# Introduzindo o programa ao usuário e dizendo quais caracteres são permitidos
print('Tradutor Código Morse')
print(RED + 'Caracteres permitidos:')
print('A B C D E F G H I J K L M')
print('N O P Q R S T U V W X Y Z')
print('0 1 2 3 4 5 6 7 8 9' + RESET)

# Recebendo a mensagem do usuário e automaticamento transformando
# todos os caracteres em letras maiúsculas, para não ter problema
# na hora de comparar com o dicionário
mensagem = input('\nDigite a mensagem que quer traduzir: ').upper()

# Dividindo mensagem para um espaço adicional entre palavras
msg_dividida = mensagem.split(' ')

# Criando um dicionário para adicionar o código morse
tradutor = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
            'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...',
            'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
            }

# Criando uma nova mensagem para ir adicionando a mensagem em código
nova_msg = ''

contador = 0  # contador para passar em todas as palavras da mensagem

print(RED + '\nMensagem em Código Morse:' + RESET)
for x in msg_dividida:
    for w in msg_dividida[contador]:
        for z in tradutor.keys():
            if w == z:
                w = tradutor[z]
                nova_msg += w + ' '
    nova_msg += '  '
    contador += 1

print(nova_msg)
