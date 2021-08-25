#  -------- Boolean  -------------
# [1]  in programming you need to know if your code output is true oe false
# [2] Boolean Values Are The Two Constant Object  True Or False
#
# ---------------------------------------

name = " "
print(name.isspace())

print("=" * 50)

print(100 > 200)
print(100 > 100)
print(100 > 90)

print("=" * 50)

#  True Values
print(bool("Osama"))
print(bool(100))
print(bool(100.52))
print(bool([1, 2, 3, 4]))
print(bool(True))


# False Values    Or Any Empty Value

print(bool(0))
print(bool(""))
print(bool(''))
print(bool([]))    # Empty list
print(bool(False))
print(bool(()))   # empty Tuple
print(bool({}))   # empty set or dictionary
print(bool(None))

# ------------------------------------------
#   Boolean Operator
#  -----------------------
# and
# or
#  not
# -------------------------------------------

age = 25
country = " Egypt"
rank = 10

print(age > 15 and country == "Egypt" and rank > 0)  # True
print(age > 15 and country == "KSA" and rank > 0)  # false

print(age > 15 or country == "Egypt")  # True
print(age > 40 or country == "KSA")   # False

print(age > 15)  # True
print(not age > 15)  # Not True = false


# -------------------------
#  Assignment Operators
# =
# +=
# -=
# *=
# /=
# **=
# %=
# ----------------------

x = 10  # Var One
y = 20  # Var Two
x = x + y    # X+ = y    # Var One = Self [operator +] Var Two
print(x)
