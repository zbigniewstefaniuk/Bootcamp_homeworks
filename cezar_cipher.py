import string

LETTERS_IN_ALPHABET = 26

def szyfruj_cezar(text: str) -> str:
    """
    Encrypts the text given as an argument according to the Caesar algorithm.

    :param text: string to encrypt.
    :return: encripted text.

    """
    cipher = []
    big_letters = list(string.ascii_uppercase)
    small_letters = list(string.ascii_lowercase)

    for letter in text:
        if letter in big_letters:  # lub if letter.isupper()
            new_letter = big_letters[(big_letters.index(letter)+3) % LETTERS_IN_ALPHABET]
        elif letter in small_letters:  # lub if letter.islower()
            new_letter = small_letters[(big_letters.index(letter)+3) % LETTERS_IN_ALPHABET]
        else:
            new_letter = letter

        cipher.append(new_letter)

    return "".join(cipher)
