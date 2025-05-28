def is_string(message):
    if type(message) is not str:
        return False
    else:
        return True

def hill_validation_plain(message):
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

def hill_validation_cypher(message):
    if not is_string(message):
        return f"Eroare, {message} nu este un sir de caractere."

    valid_chars = [""]

    for LOWER_letter in range(97, 123):
        valid_chars.append(chr(LOWER_letter))

    for letter in message:
        if letter not in valid_chars:
            return "Eroare, mesajul tău conține caractere invalide."

    return message

def minor(matrix, order, row, column):
    result_matrix = []
    for i in range(order):
        add_row = []
        for j in range(order):
            if i == row or j == column:
                continue
            else:
                add_row.append(matrix[i][j])
        if i == 0:
            pass
        else:
            result_matrix.append(add_row)

    return result_matrix

def second_order_det(matrix):
    i = 0
    j = 0
    return (matrix[i][j] * matrix[i+1][j+1]) - (matrix[i][j+1] * matrix[i + 1][j])

def third_order_det(matrix):
    sum_of_determinant = 0
    for i in range(1):
        for j in range(3):
            minor_of_det = minor(matrix, 3, i, j)
            sign = pow(-1, i + j + 2)
            result = matrix[i][j] * sign * second_order_det(minor_of_det)
            sum_of_determinant += result
    return sum_of_determinant

def key_validation_hill(key):
    key_len = len(key)

    if not is_string(key):
        return f"Eroare, {key} nu este un sir de caractere."

    if key_len != 4 and key_len != 9:
        return f"Cheia {key} nu are strict 4 sau 9 caractere."
    elif key_len == 4:
        square_matrix2 = []
        k = 0

        for i in range(2):
            row = []
            for j in range(2):
                row.append(ord(key[k]))
                k += 1
            square_matrix2.append(row)


        delta = second_order_det(square_matrix2)

        if delta == 0:
            return f"Matricea {square_matrix2} nu este inversabilă, determinantul este egal cu {delta}."
        else:
            return key

    else:
        square_matrix3 = []
        k = 0

        for i in range(3):
            row = []
            for j in range(3):
                row.append(ord(key[k]))
                k += 1
            square_matrix3.append(row)

        delta = third_order_det(square_matrix3)

        if delta == 0:
            return f"Matricea {square_matrix3} nu este inversabilă, pentru că determinantul este egal cu: {delta}."
        else:
            return key