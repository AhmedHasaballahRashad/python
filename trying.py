

myF = ["Os", "Ah", "Ga", "Al", "Ra", "Sa", "Ta", "Ma", "Mo", "Wa"]

print(len(myF))   # List Length  [10]

a = 0
while a < len(myF):  # a < 10
    print(f"#{str(a+1).zfill(2)} {myF[a]}")
    a += 1             # a = a +1
print("All Names Is Printed On Screen ")
