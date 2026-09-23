from decimal import Decimal

# decimal context manger

print(0.1 + 0.1 + 0.1 - 0.3)
# problem it will give 5.551115123125783e-17 not correct answer

print(Decimal("0.1") + Decimal("0.1") + Decimal("0.1") - Decimal("0.3"))

from fractions import Fraction

myf = Fraction(2, 7)
print(myf)
