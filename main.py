from tika import parser

# dictionaries containing morse code and most keyboard symbols
morse_dict = {'a': '*-',
              'b': '-***',
              'c': '-*-*',
              'd': '-**',
              'e': '*',
              'f': '**-*',
              'g': '--*',
              'h': '****',
              'i': '**',
              'j': '*---',
              'k': '-*-',
              'l': '*-**',
              'm': '--',
              'n': '-*',
              'o': '---',
              'p': '*--*',
              'q': '--*-',
              'r': '*-*',
              's': '***',
              't': '-',
              'u': '**-',
              'v': '***-',
              'w': '*--',
              'x': '-**-',
              'y': '-*--',
              'z': '--**',
              '1': '*----',
              '2': '**---',
              '3': '***--',
              '4': '****-',
              '5': '*****',
              '6': '-****',
              '7': '--***',
              '8': '---**',
              '9': '----*',
              '0': '-----',
              '.': '*-*-*-',
              ',': '--**--',
              ':': '---***',
              '?': '**--**',
              "'": '*----*',
              '-': '-****-',
              '/': '-**-*',
              '(': '-*--*-',
              ')': '-*--*-',
              '"': '*-**-*',
              ' ': ' '
              }
symbol_dict = {'`': 'grave accent',
               '~': 'tilde',
               '!': 'exclamation mark',
               '@': 'at sign',
               '#': 'hash',
               '$': 'dollar sign',
               '%': 'percent sign',
               '^': 'carat',
               '&': 'and',
               '*': 'asterisk',
               '-': 'hyphen',
               '_': 'underscore',
               '=': 'equal sign',
               '+': 'plus sign',
               '[': 'open bracket',
               ']': 'close bracket',
               '{': 'open brace',
               '}': 'close brace',
               '|': 'vertical pipe',
               ';': 'semicolon',
               '<': 'less than',
               '>': 'greater than',
               }

# read pdf file
raw = parser.from_file('sample.pdf')
text_file = raw['content']

encoded_file = ''

# check for official morse code characters
for character in text_file:
    if character.lower() in morse_dict:
        encoded_file += morse_dict[character.lower()]
        encoded_file += ' '

    # check for common keyboard symbols
    # replace the symbol with description
    elif character in symbol_dict:
        symbol = symbol_dict[character]

        # convert description into morse code
        for symbol_character in symbol:
            if character.lower() in morse_dict:
                encoded_file += morse_dict[character.lower()] + ' '
    else:
        encoded_file += '   '

# write encoded text into file
with open('morse.txt', 'w') as file:
    file.write(encoded_file.strip())
