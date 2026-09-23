# -------------------------
# Number Bases / Literals
# -------------------------

# Python supports different number systems:
# Decimal  -> Base 10
# Binary   -> Base 2
# Octal    -> Base 8
# Hex      -> Base 16


# -------------------------
# Octal
# -------------------------

# Prefix 0o means the number is written in octal (base 8).
# 20 (octal) = 16 (decimal)

octal = 0o20

print(octal)
# Output: 16


# -------------------------
# Hexadecimal
# -------------------------

# Prefix 0x means the number is written in hexadecimal (base 16).
# FF (hexadecimal) = 255 (decimal)

hexadecimal = 0xFF

print(hexadecimal)
# Output: 255


# -------------------------
# Binary
# -------------------------

# Prefix 0b means the number is written in binary (base 2).
# 1000 (binary) = 8 (decimal)

binary = 0b1000

print(binary)
# Output: 8


# -------------------------
# Decimal → Other Bases
# -------------------------

# oct() converts a decimal integer to an octal string.
print(oct(16))
# Output: '0o20'


# hex() converts a decimal integer to a hexadecimal string.
print(hex(255))
# Output: '0xff'


# bin() converts a decimal integer to a binary string.
print(bin(8))
# Output: '0b1000'


# -------------------------
# Other Base → Decimal
# -------------------------

# int(value, base) converts a number written as a string
# from the given base into a decimal integer.

print(int('16', 8))
# '16' is written in base 8
# Output: 14
#
# 1 × 8 + 6 × 1 = 14