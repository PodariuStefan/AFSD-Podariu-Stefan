def is_string(message):
    if type(message) is not str:
        return False
    else:
        return True

def enigma_validation_cypher_plain(message):
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

def check_whitespaces(space):
    counter = 0
    used_chars = []
    white_space_count = 0

    for i in range(len(space)):
        if space[i] in used_chars:
            return f"Eroare, \"{space[i]}\" nu are voie să se repete."

        if space[i] != " ":
            counter += 1
            used_chars.append(space[i])
            white_space_count = 0
        else:
            if counter == 1:
                return f"Eroare, caracterul \"{space[i - 1]}\" nu are pereche."

            counter = 0
            white_space_count += 1

        if white_space_count == 2 or counter == 3:
            return f"Eroare, \"{space[i]}\" nu respecta cerintele de formatare"

    if counter == 1:
        return f"Eroare, \'{space[-1]}\' nu are pereche"

    return space

def plugboard_validation(key):
    groups = []

    if not is_string(key):
        return f"Eroare, {key} nu este un sir de caractere."

    if check_whitespaces(key) != key:
        return check_whitespaces(key)

    for i in range(0, len(key), 2):
        groups = key.split(" ")

    return groups

def from_array2dict(arr):
    enigma_dict = {}

    for i in range(len(arr)):
        enigma_dict.update({arr[i][0] : arr[i][1]})

    return enigma_dict