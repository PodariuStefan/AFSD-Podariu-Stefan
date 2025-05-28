def is_string(message):
    if type(message) is not str:
        return False
    else:
        return True

def rc4_validation_plain(message):
    if is_string(message):
        return message
    else:
        return f"Eroare, {message} nu este un sir de caractere."

def rc4_validation_cypher(message):
    if not(is_string(message)):
        return f"Eroare, {message} nu este un sir de caractere."

    if message[0] != 0 and message[1] != 'x':
        return "Acest sir de caractere nu respectă regulile hexazecimale de formatare."
    else:
        pass

    valid_chars = []

    for LOWER_letter in range(97, 103):
        valid_chars.append(chr(LOWER_letter))

    for digit in range(48, 58):
        valid_chars.append(chr(digit))

    for i in range(2, len(message)):
        if message[i] not in valid_chars:
            return "Eroare, mesajul tău conține caractere invalide."
        else:
            pass

    return message

def key_validation_rc4(key):
    if is_string(key):
        return key
    else:
        return f"Eroare, {key} nu este un sir de caractere."

def rc4_validation(message, mod, key):
    error_statement = "Nu au fost îndeplinite toate condițiile de formatare"

    if key_validation_rc4(key) != key:
        return error_statement

    if mod == "criptare":
        return rc4_validation_plain(message)

    elif mod == "decriptare" or mod == "spargere":
        return rc4_validation_cypher(message)

    else:
        return "Modul ales nu este valid."