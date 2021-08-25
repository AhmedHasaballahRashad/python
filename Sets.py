# Not Ordered and not Indexed
mySetOne = {"Ahmed", "Osama", 100}
print(mySetOne)

# Slicing can not be done
#mySettwo = {1, 2, 3, 4, 5}
# print(mySettwo[0:3])

# Has Only Immutaple data type
mySetthree = {"Ahmed", 100, 100.5, True}
print(mySetthree)


# Clear
a = {1, 2, 3}
a.clear()
print(a)

# Union
b = {"One", "Two", "Three"}
c = {"1", "2", "3"}
x = {"Zero", "Nine"}
print(b | c)
print(b.union(c, x))

# Add
d = {1, 2, 3, 4}
d.add(5)
print(d)

# Copy
e = {1, 2, 3, 4}
f = e.copy()
e.add(5)
print(e)
print(f)

g = {1, 2, 3, 4, 5, 6}
g.remove(4)
# g.remove(7)   # KeyError: 7 >>>  Error because number not found in set
print(g)

#  Discard ()
h = {1, 2, 3, 4, 5, 6}
h.discard(4)
h.discard(7)
print(h)

# Pop
i = {"A", True, 1, 2, 3, 4, 5, 6}
print(i.pop())

# Update
j = {1, 2, 3, 4}
k = {1, "One", "Two", 2}
j.update(k)
j.update(["Html", "Css"])
print(j)

# Difference
a = {1, 2, 3, 4}
b = {1, 2, "Osama", "Ahmed"}
print(a)
print(b.difference(a))   # = a - b
print(a)

print("=" * 40)   # Separator

# Difference_Update

c = {1, 2, 3, 4}
d = {1, 2, "Osama", "Ahmed"}
print(c)
c.difference_update(d)  # = c - d
print(c)
print("=" * 40)   # Separator

# intersection
e = {1, 2, 3, 4, "Osama", "X"}
f = {"Osama", "X", 2}
print(e)
print(e.intersection(f))  # e & f
print(e)

# intersection_update
g = {1, 2, 3, 4, "Osama", "X"}
h = {"Osama", "X", 2}
print(g)
g.intersection_update(h)  # e & f
print(g)

print("=" * 40)   # Separator

# symmetric_difference()

i = {1, 2, 3, 4, 5, "X"}
j = {"Osama", "Zero", 1, 2, 4}
print(i)
print(i.symmetric_difference(j))   # i ^ j
print(i)

print("=" * 40)   # Separator

# symmetric_difference_update()
k = {1, 2, 3, 4, 5, "X"}
l = {"Osama", "Zero", 1, 2, 4}
print(k)
k.symmetric_difference_update(j)   # i ^ j
print(k)


# issuperset()
a = {1, 2, 3, 4}
b = {1, 2, 3}
c = {1, 2, 3, 4, 5}
print(a.issuperset(b))  # True
print(a.issuperset(c))  # False

print("="*50)

# issubset()
d = {1, 2, 3, 4}
e = {1, 2, 3}
f = {1, 2, 3, 4, 5}
print(d.issubset(e))  # True
print(d.issubset(f))  # False

print("="*50)

# isdisjoint()
g = {1, 2, 3, 4}
h = {1, 2, 3}
i = {10, 11, 12}
print(g.isdisjoint(h))  # True
print(g.isdisjoint(i))  # False
