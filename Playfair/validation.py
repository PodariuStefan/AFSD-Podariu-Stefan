def is_string(message):
    if type(message) is not str:
        return False
    else:
        return True

def playfair_validation_plain(message):
    if not is_string(message):
        return f"Eroare, {message} nu este un sir de caractere."

    valid_chars = [" "]

    for LOWER_letter in range(97, 123):
        valid_chars.append(chr(LOWER_letter))

    for UPPER_letter in range(65, 91):
        valid_chars.append(chr(UPPER_letter))

    for letter in message:
        if letter not in valid_chars:
            return "Eroare, mesajul tău conține caractere invalide."

    return message

def playfair_validation_cypher(message):
    if not is_string(message):
        return f"Eroare, {message} nu este un sir de caractere."

    valid_chars = []

    for LOWER_letter in range(97, 123):
        valid_chars.append(chr(LOWER_letter))

    for letter in message:
        if letter not in valid_chars:
            return "Eroare, mesajul tău conține caractere invalide."

    return message

def key_validation_playfair(key):
    if not is_string(key):
        return f"Eroare, {key} nu este un sir de caractere."

    valid_chars = []
    used_chars = []

    for LOWER_letter in range(97, 123):
        valid_chars.append(chr(LOWER_letter))

    for letter in key:
        if letter in used_chars:
            letter_freq = key.count(letter)
            return f"Eroare, cheia nu poate avea caractere care se repetă, caracterul \"{letter}\" a fost găsit de {letter_freq} ori."
        if letter not in valid_chars:
            return "Eroare, mesajul tău conține caractere invalide."
        used_chars.append(letter)

    return key

def playfair_validation(message, mod, key):
    error_statement = "Nu au fost îndeplinite toate condițiile de formatare"
    if key_validation_playfair(key) != key:
        return error_statement

    if mod == "criptare":
        return playfair_validation_plain(message)

    elif mod == "decriptare":
        return playfair_validation_cypher(message)

    else:
        return "Modul ales nu este valid."
