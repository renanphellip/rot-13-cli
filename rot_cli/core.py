from string import ascii_lowercase


def encrypt(text: str, rot: int):
    """Encrypts the text."""
    encrypted = ''
    for char in text:
        char = char.lower()
        if char == ' ':
            encrypted += char
        elif char not in ascii_lowercase:
            ...
        else:
            pos = ascii_lowercase.find(char) + rot
            char = ascii_lowercase[pos % 26]
            encrypted += char
    return encrypted


def decrypt(cipher: str, rot: int):
    """Decrypts the cipher."""
    decrypted = ''
    for char in cipher:
        char = char.lower()
        if char == ' ':
            decrypted += char
        elif char not in ascii_lowercase:
            ...
        else:
            pos = ascii_lowercase.find(char) - rot
            char = ascii_lowercase[pos % 26]
            decrypted += char
    return decrypted
