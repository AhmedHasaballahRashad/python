# -----------------------
# Membership Operators
#  in
# Not in
# --------------------

# String
from os import stat
from typing import Counter


Name = "Ahmed"
print("s" in Name)
print("A" in Name)

print("#" * 50)

# List
friends = ["Ahmed", "Mahmoud", "Osama"]
print("Osama" in friends)
print("Ahmed" in friends)
print("Mahmoud" not in friends)

print("#" * 50)


# Using In And Not In  With Condition
CountriesOne = ["Egypt", "KSA", "Kuwait", "Bahrain"]
CountriesOneDiscount = 80

CountriesTwo = ["Italy", "France"]
CountriesTwoDiscount = 50

country = input("enter your country : ").strip().capitalize()

if country in CountriesOne:
    print(f"You Are from {country} And Have Discount {CountriesOneDiscount}")
elif country in CountriesTwo:
    print(f"You Are From {country} And Have Discount {CountriesTwoDiscount}")
else:
    print("Country Is Not Found In List ")


# ----------------------------------
#  Practical Membership Control
# ----------------------------------

#  List Contains Admins


admins = ["Ahmed", "Osama", "Sameh", "Manal", "Rahma", "Mahmoud", "Enas"]

# Login
name = input("Please Type Your Name ").strip().capitalize()

#  If Name Is In Admin
if name in admins:
    print(f"Hello {name} Welcome Back ")

    option = input("Delete Or Update Your Name ? ").strip().capitalize()
    print(option)

    # Update Option
    if option == "Update" or option == "U":
        theNewName = input("Your New Name Please : ").strip().capitalize()

        admins[admins.index(name)] = theNewName

        print("Name Updated.")
        print(admins)

        # Delete Option
    elif option == "Delete" or option == "D":
        admins.remove(name)
        print("Name Deleted.")
        print(admins)

        # Wrong Option
    else:
        print("Wrong Option")

else:

    status = input("Not Admin, Add You Or Not ").strip().capitalize()
    if status == "Yes" or status == "Y":
        print("You Have Been Added ")
        admins.append(name)
        print(admins)

    else:
        print("You Are Not Added ")
