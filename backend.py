
class Cipher(object):

    @staticmethod
    def vigenere(plaintext, key, version=1):

        if version == 0:
            return Cipher.vigenere_simple(plaintext, key)
        elif version == 1:
            return Cipher.vigenere_upper(plaintext, key)
        elif version == 2:
            return Cipher.vigenere_alpha(plaintext, key)
        elif version == 3:
            return Cipher.vigenere_alpha_numeric(plaintext, key)

    @staticmethod
    def vigenere_simple(plaintext, key):

        ASCII_MIN = 32
        ASCII_MAX = 126

        ciphertext = ""
        key_index = 0

        for letter in plaintext:

            if key_index == len(key):
                key_index = 0

            substitute = ord(letter) + ord(key[key_index])
            while substitute > ASCII_MAX:
                substitute -= ASCII_MAX - ASCII_MIN + 1

            ciphertext += chr(substitute)
            key_index += 1
        
        return ciphertext

    @staticmethod
    def vigenere_upper(plaintext, key):

        CAPITAL_LETTER_MIN = 65
        CAPITAL_LETTER_MAX = 90

        plaintext = plaintext.upper()
        key = key.upper()
        ciphertext = ""
        key_index = 0

        for letter in plaintext:

            print('Plaintext:  ', letter)
            
            if (ord(letter) < 65) or (ord(letter) > 90):
                ciphertext += letter
                continue

            if key_index == len(key):
                key_index = 0
            print('Key:        ', key[key_index])

            substitute = ord(letter) + ord(key[key_index]) - CAPITAL_LETTER_MIN
            while substitute > CAPITAL_LETTER_MAX:
                substitute -= CAPITAL_LETTER_MAX - CAPITAL_LETTER_MIN + 1

            ciphertext += chr(substitute)
            print('Ciphertext: ', chr(substitute))
            key_index += 1

        return ciphertext

    @staticmethod
    def vigenere_alpha(plaintext, key):

        CAPITAL_LETTER_MIN = 65
        CAPITAL_LETTER_MAX = 90
        LOWER_LETTER_MIN = 97
        LOWER_LETTER_MAX = 122

        return "Placeholder (not coincidence)"

    @staticmethod
    def vigenere_alpha_numeric(plaintext, key):

        NUMBER_MIN = 48
        NUMBER_MAX = 57
        CAPITAL_LETTER_MIN = 65
        CAPITAL_LETTER_MAX = 90
        LOWER_LETTER_MIN = 97
        LOWER_LETTER_MAX = 122

        SUBSTITUTE_MIN = CAPITAL_LETTER_MIN - (NUMBER_MAX - NUMBER_MIN) - 1
        SUBSTITUTE_MAX = CAPITAL_LETTER_MAX + \
            (LOWER_LETTER_MAX - LOWER_LETTER_MIN) + 1

        return "Placeholder (not coincidence)"