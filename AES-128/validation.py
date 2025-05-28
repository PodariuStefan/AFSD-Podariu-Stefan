def is_string(message):
    if type(message) is not str:
        return False
    else:
        return True

def aes128_validation_plain(message):
    if is_string(message):
        return message
    else:
        return f"Eroare, {message} nu este un sir de caractere."

def aes128_validation_cypher(message):
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

def key_validation_aes128(key):
    key_len = len(key)
    if not is_string(key):
        return f"Eroare, {key} nu este un sir de caractere."
    if key_len != 16:
        return f"Cheia {key} nu are strict 16 caractere"
    return key

def aes128_validation(message, mod, key):
    error_statement = "Nu au fost îndeplinite toate condițiile de formatare"

    if key_validation_aes128(key) != key:
        return error_statement

    if mod == "criptare":
        return aes128_validation_plain(message)

    elif mod == "decriptare":
        return aes128_validation_cypher(message)

    else:
        return "Modul ales nu este valid."