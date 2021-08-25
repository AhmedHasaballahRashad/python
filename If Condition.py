# -------------------------
# -- Control Flow -------
# -- If , Elif , else ---
# --- Make Decisions ----
# ------------------------

uName = "Ahmed"
uCountry = "Ksa"
isStudent = "Yes"
cName = "Python Course"
cPrice = 100

if uCountry == "Egypt" or uCountry == "KSA":
    print(f"Hello {uName} Because You Are From {uCountry}")
    if isStudent == "yes":
        print(f"Hello {uName} Because You Are From {uCountry} And Student ")
        print(f"The Course \"{cName}\" Price is : {cPrice-90}")
    else:
        print(f"Hello {uName} Because You Are From {uCountry}")
        print(f"The Course \"{cName}\" Price is : {cPrice-80}")

elif uCountry == "Kuwait" or uCountry == "bahrain":
    print(f"Hello {uName} Because You Are From {uCountry}")
    print(f"The Course \"{cName}\" Price is : {cPrice-50}")
else:
    print(f"Hello {uName} Because You Are From {uCountry}")
    print(f"The Course \"{cName}\" Price is : {cPrice-30}")

  #  Ternary If
movieRate = 18
age = 16
if age < movieRate:
    print("Movie S Not Good For You ")  # Condition If True
else:
    print("Movie S  Good For You And Happy Watching ")  # Condition If False

print("Movie S Not Good For You" if age <
      movieRate else "Movie S  Good For You And Happy Watching")
# Condition If True | If Condition | Else | Condition If False

# -------------------------------------
# ----- Calculate Age Advanced  -------
# -------------------------------------
#   Write Notes
print("#" * 80)
print(" You Can Write The First Letter Or Full Name Of The Time Unit ".center(80, '*'))
print("#" * 80)
# Collect Age Data
age = input("Please Write Your Age ")

# Collect Time Unit Data
unit = input("Please Choose Time Unit : Months ,Weeks , Days ").strip().lower()

# Get Time Units
months = int(age) * 12
Weeks = months * 4
days = int(age) * 365

if unit == 'months' or unit == "m":
    print("You Choosed The Unit Months")
    print(f"You Lived For {months:,} Months.")

elif unit == 'weeks' or unit == "w":
    print("You Choosed The Unit Weeks")
    print(f"You Lived For {Weeks:,} Weeks.")

elif unit == 'days' or unit == "d":
    print("You Choosed The Unit Days ")
    print(f"You Lived For {days:,} Days.")
