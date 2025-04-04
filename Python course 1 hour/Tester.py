import random
def column_generator(num):
    random_numbers = []
    for i in range(8):
        random_numbers.append(random.randint(10, 200))
    return print(random_numbers)

column_generator(6)