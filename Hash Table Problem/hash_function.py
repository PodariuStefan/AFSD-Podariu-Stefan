from collections import defaultdict

global hash_keys
global hash_map
hash_map = defaultdict(list)

def hash_mapper(value):
    current_sum = 0
    for i in range((len(value)-1)//3):
        current_sum += float(value[i:i+3])
        i += 3
    total = (int(current_sum) + int(value[-1])) % 1000
    hash_map[total].append(value)