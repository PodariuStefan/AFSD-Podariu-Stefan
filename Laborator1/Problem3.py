# Cerință
# Într-un grup sunt n prieteni. Când se întâlnesc se salută, fiecare dând mâna cu toți ceilalți.

# Câte strângeri de mână au loc?

import math

def factorial (n):
    if n <= 2:
        return 1
    else:
        return n * factorial(n-1)

factorial (4)