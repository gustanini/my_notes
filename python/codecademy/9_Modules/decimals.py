# Import Decimal below:
from decimal import Decimal

# Fix the floating point math below:

#two_decimal_points = 0.2 + 0.69
#print(two_decimal_points)

#four_decimal_points = 0.53 * 0.65
#print(four_decimal_points)

# Use Decimal to make two_decimal_points only have two decimals points and four_decimal_points to only have four decimal points.

two_decimal_points = Decimal('0.2') + Decimal('0.69')
print(two_decimal_points)

four_decimal_points = Decimal('0.53') * Decimal('0.65')
print(four_decimal_points)