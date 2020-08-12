import winsound
import time

char_to_dots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}

dots_to_char = {v: k for k, v in char_to_dots.items()}

def encode(x):
    global char_to_dots
    x = x.upper()
    y = []
    for i in range(len(x)):
        y.append(char_to_dots[x[i]])
    print(' '.join(y))


def decode(x):
    global dots_to_char
    x = x.split()
    y = []
    for i in range(len(x)):
        y.append(dots_to_char[x[i]])
    print(''.join(y))
    x = ''.join(x)
    for i in range(len(x)):
        if x[i] == '.':
            winsound.Beep(200, 400)
        elif x[i] == '-':
            winsound.Beep(600, 400)
        time.sleep(0.5)

while True:
    z = input('Encode or decode morse? (E/D)\n')
    if z == 'E':
        omega = input('Encode:\n')
        encode(omega)
    elif z == 'D':
        omega = input('Decode:\n')
        decode(omega)
