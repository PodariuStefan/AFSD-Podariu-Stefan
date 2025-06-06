from variables import *
from hash import *

def is_valid(solution):
    if ((solution.count(string.ascii_lowercase) < 4) and
        (solution.count(string.ascii_uppercase) < 2) and
        (solution.count(string.digits) < 2) and
        (solution.count("@!#$") < 2)):
        return True
    else:
        return False

def backtrack(solution, count = 0):
    if len(solution) == target_len and is_valid(solution):
        hash_pass = get_hash(solution)
        print(f"Pentru sirul {solution} avem valoarea hash {hash_pass}.")
        if hash_pass == target2:
            print(f"\nParola găsită: {solution}\n"
                  f"Număr apeluri recursive: {count}")
            exit(1)
        return

    for character in viable_chars:
        count += 1
        backtrack(solution + character, count)
