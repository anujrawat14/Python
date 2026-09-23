# -------------------------
# Complex Numbers
# -------------------------

# Complex number
complex_num = 2 + 1j

print(complex_num)
# Output: (2+1j)


# Addition
print(complex_num + 2)
# Output: (4+1j)


# Multiplication by an integer
print(complex_num * 2)
# Output: (4+2j)


# Another complex number
new_complex = 2 + 2j


# Multiplication of two complex numbers
print(complex_num * new_complex)
# Output: (2+1j) * (2+2j)
#        = 4 + 4j + 2j + 2j²
#        = 4 + 6j - 2
#        = 2 + 6j
#
# Output: (2+6j)


# Complex exponentiation
print(complex_num**new_complex)
# Python can calculate complex powers as well.
# The result will generally be a complex number.

z = 3 + 4j

# Real part
print(z.real)
# 3.0


# Imaginary part
print(z.imag)
# 4.0


# Complex conjugate
print(z.conjugate())
# (3-4j)


# Absolute value / magnitude
print(abs(z))
# 5.0
