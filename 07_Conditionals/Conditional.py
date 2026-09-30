# =========================
# Conditional Statements
# =========================

# A conditional statement is used to execute
# different code based on a condition.


# =========================
# 1. if
# =========================

age = 20

if age >= 18:
    print("You are an adult")


# =========================
# 2. if-else
# =========================

age = 16

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")


# =========================
# 3. if-elif-else
# =========================

marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# =========================
# 4. Multiple Conditions
# =========================

age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")


# =========================
# 5. Nested if
# =========================

age = 20
has_ticket = True

if age >= 18:
    if has_ticket:
        print("You can enter")
    else:
        print("Ticket required")
else:
    print("You must be 18 or older")


# =========================
# 6. Comparison Operators
# =========================

# ==   Equal to
# !=   Not equal to
# >    Greater than
# <    Less than
# >=   Greater than or equal to
# <=   Less than or equal to


# =========================
# 7. Logical Operators
# =========================

# and → both conditions must be True
# or  → at least one condition must be True
# not → reverses the condition

age = 20

if age >= 18 and age <= 60:
    print("Working age")


# =========================
# 8. Membership in Condition
# =========================

tea = "Green"

if tea in ["Green", "Black", "Oolong"]:
    print("Tea is available")


# =========================
# 9. Truthy / Falsy
# =========================

name = ""

if name:
    print("Name is available")
else:
    print("Name is empty")