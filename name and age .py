# --------------------------
# -- User Input ---------

fName = input("What\'s Your First Name : ")
mName = input("What\'s Your Middle Name : ")
lName = input("What\'s Your Last Name : ")

#   We Can Make Chain Of methods
fName = fName.strip().capitalize()
mName = mName.strip().capitalize()
lName = lName.strip().capitalize()
print(f"Hello {fName} {mName:1s} {lName} Happy To see You")
#print("Hello {} {} {} Happy To see You".format(fName, mName, lName))

print("#" * 50)

theName = input("What\'s Your Name : ").strip().capitalize()
theMail = input("What\'s Your Email : ").strip()
theUsername = theMail[0:theMail.index("@")]
theWebsite = theMail[theMail.index("@")+1:]

print(f"Hello {theName} Your Email is : {theMail}")
print(f"Your Username is {theUsername} \nYour Website is {theWebsite}")

# -----------------
#   practical full age details

# Input Age
age = int(input("What\'s Your Age : ").strip())

# Get Age in All Details
months = age * 12
weeks = months * 4
days = months * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print("You Lived For:")
print(f"{age*12} Months.")  # :, to make seprator  between numbers
print(f"{weeks:,} Weeks.")
print(f"{days:,} Days.")
print(f"{hours:,} Hours.")
print(f"{minutes:,} Minutes.")
print(f"{seconds:,} Seconds")

input("Thank You For Your Time")  # to stop running screen
