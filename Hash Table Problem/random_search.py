import random

def rand_choice_1000(arr):
    random_arr = random.choices(arr, k=1000)
    return random_arr

def linear_search(target, hash_tab):
    for keys in list(hash_tab):
        iterations = 0
        for cnps in list(hash_tab[keys]):
            if cnps == target:
                print(f"{target} has been found after {iterations} searches with the hash value of: {keys}")
                iterations += 1
                break
            iterations += 1