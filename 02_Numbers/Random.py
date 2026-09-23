# -------------------------
# Random Module
# -------------------------

import random

# -------------------------
# Random Float
# -------------------------

# random() returns a random floating-point number
# between 0.0 (inclusive) and 1.0 (exclusive).

random_number = random.random()

print(random_number)
# Example output: 0.4738291


# -------------------------
# Random Integer
# -------------------------

# randint(a, b) returns a random integer
# between a and b, INCLUDING both endpoints.

random_number = random.randint(1, 10)

print(random_number)
# Possible output: 1, 2, 3, ..., 10


# -------------------------
# Random Choice
# -------------------------

# choice() randomly selects one element
# from a sequence such as a list, tuple, or string.

random_number = random.choice([1, 2, 3])

print(random_number)
# Possible output: 1, 2, or 3


# -------------------------
# Shuffle
# -------------------------

# shuffle() randomly rearranges the elements
# of a list IN PLACE.
#
# It modifies the original list and returns None.

numbers = [1, 2, 3, 4]

random.shuffle(numbers)

print(numbers)
# Example output: [3, 1, 4, 2]