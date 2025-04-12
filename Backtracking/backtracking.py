from variables import *
from hash import *

def is_valid(solution):
    if ((solution.count(string.ascii_lowercase) < 4) and
        (solution.count(string.ascii_uppercase) < 2) and
        (solution.count(string.digits) < 2) and
        (solution.count("@!#$") < 2)):
        return True

def backtrack(solution, index):
    if len(solution) == target_len and is_valid(solution):
        hash_pass = get_hash(solution)
        if hash_pass == target:
            print(f"Parola găsită: {solution}\n"
                  f"Număr apeluri recursive: {index}")
            exit(1)
        return

    for character in viable_chars:
        backtrack(solution + character, index + 1)
