"""
    AVALIAÇÃO 02(POO) - TRADUTOR CÓDIGO MORSE
    BEATRIZ VIDAL FREIRE - P7 DE INFORMÁTICA, IFCE CAMPUS FORTALEZA
"""
print('Tradutor Código Morse')
print('Caracteres permitidos:')
print('A B C D E F G H I J K L M')
print('N O P Q R S T U V W X Y Z')
print('0 1 2 3 4 5 6 7 8 9')

mensagem = input('\nDigite a mensagem que quer traduzir: ').upper()
msg_dividida = mensagem.split(' ')

tradutor = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
            'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...',
            'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
            }

nova_msg = ''
contador = 0

print('Mensagem em Código Morse:')
for x in msg_dividida:
    for w in msg_dividida[contador]:
        for z in tradutor.keys():
            if w == z:
                w = tradutor[z]
                nova_msg += w + ' '
    nova_msg += '  '
    contador += 1

print(nova_msg)
