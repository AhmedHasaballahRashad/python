
#    Tuples

myTupleOne = ("Ahmed", "Hasaballah")
myTupleTwo = "Ahmed", "Hasaballah"

print(myTupleOne)
print(myTupleTwo)

print(type(myTupleOne))
print(type(myTupleTwo))

myTupleThree = (1, 2, 3, 4, 5, 6)
print(myTupleThree[3])
print(myTupleThree[1+2])

myTuplefour = (1, 2, 3, 4, 5)
# myTuplefour[2] = "three"     # 'tuple' object does not support item assignment
print(myTuplefour)

myTuplefive = ("Ahmed", "Ahmed", 1, 2, 30.55, False)
print(myTuplefive[1])
print(myTuplefive[-1])


myTuple1 = ("Ahmed",)    # Tuple With ONE Elemant
myTuple2 = "Ahmed",
print(myTuple1)
print(myTuple2)
print(type(myTuple1))
print(type(myTuple1))

#   Tuple Concatenation
a = (1, 2, 3, 4)
b = (5, 6)
c = a+b
print(c)
d = a+("A", "B", True)+b
print(d)

# Tuple ,String ,List Repeat (*)
myString = "Ahmed"
myList = [1, 2]
myTuple = ("A", "B")

print(myString * 3)
print(myList * 4)
print(myTuple * 6)

# Methods => Count
b = (1, 3, 5, 6, 7, 9, 6, 7)
print(b.count(7))

# Methods => index()
c = (1, 3, 5, 6, 7, 9, 6, 7)
print("The Position of Index Is : {}".format(c.index(6)))
print(f"The Position of Index Is : {c.index(6)}")

# Tuple Destruct
a = ("A", "B", 4, "C")
x, y, _, z = a
print(x)
print(y)
print(z)
