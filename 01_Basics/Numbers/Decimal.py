# -------------------------
# Decimal
# -------------------------

from decimal import Decimal


# Floating-point numbers can have small precision errors
# because many decimal fractions cannot be represented
# exactly in binary floating-point format.

result = 0.1 + 0.1 + 0.1 - 0.3

print(result)
# Output:
# 5.551115123125783e-17
#
# Mathematically, the result should be 0.0,
# but floating-point representation causes a tiny error.


# Decimal provides exact decimal arithmetic.
#
# IMPORTANT:
# Pass decimal values as strings to Decimal().
# This avoids first creating a float with its own precision error.

result = (
    Decimal("0.1")
    + Decimal("0.1")
    + Decimal("0.1")
    - Decimal("0.3")
)

print(result)
# Output: 0.0


# -------------------------
# Fraction
# -------------------------

from fractions import Fraction


# Fraction represents a number as an exact
# numerator / denominator.

my_fraction = Fraction(2, 7)

print(my_fraction)
# Output: 2/7


# Fraction can perform exact arithmetic.

a = Fraction(1, 3)
b = Fraction(1, 6)

print(a + b)
# Output: 1/2


# Numerator and denominator can be accessed directly.

print(my_fraction.numerator)
# Output: 2

print(my_fraction.denominator)
# Output: 7