
def keyword_cipher(keyword: str, message: str) -> str:
    """_summary_:
        A Keyword Cipher functions.
        It works by replacing each letter of a message with a letter from a shifted alphabet built using a keyword

    Args:
        keyword (str): keyword to be used for encryption
        message (str): message to be encrypted

    Returns:
        str: encrypted message with all aphabetic characters in lowercase
    """

    alphabet = [chr(num) for num in range(ord('a'), ord('z') + 1)]
    alphabet_dict = {letter : index for index, letter in enumerate(alphabet)}
    cipher_alphabet = []

    for letter in keyword:
        if letter.isalpha():
            cipher_alphabet.append(letter.lower())
        else:
            raise ValueError("Invalid keyword. keyword must contain only alphabetic characters")

    for letter in alphabet:
        if letter not in cipher_alphabet:
            cipher_alphabet.append(letter)

    encrypted_message = ''
    for letter in message:
        if letter.isalpha():
            encrypted_message += cipher_alphabet[alphabet_dict[letter.lower()]]
        else:
            encrypted_message += letter

    return encrypted_message
