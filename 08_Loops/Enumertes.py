# ==============================
# enumerate() Function
# ==============================

# enumerate() is a built-in function.
# It returns an enumerate object containing
# index-value pairs from an iterable.
# The default starting index is 0.


x = ("masala", "lemon", "ginger")

y = enumerate(x)

print(y)
# <enumerate object at 0x0000023099FA0400>

print(list(y))
# [(0, 'masala'), (1, 'lemon'), (2, 'ginger')]
