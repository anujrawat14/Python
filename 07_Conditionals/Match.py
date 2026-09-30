# =========================
# Match Statement
# =========================

# Python does not have a traditional "switch" statement.
# Instead, Python uses the "match" statement.
#
# match is used when we want to compare one value
# against multiple possible patterns/values.
#
# It is similar to switch in languages like Java, C, and C++.


# =========================
# Basic Example
# =========================

day = 2

match day:

    case 1:
        print("Monday")

    case 2:
        print("Tuesday")

    case 3:
        print("Wednesday")

    case 4:
        print("Thursday")

    case 5:
        print("Friday")

    case 6:
        print("Saturday")

    case 7:
        print("Sunday")

    case _:
        print("Invalid day")