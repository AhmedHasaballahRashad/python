
myList = ["One", "Two", "One", 1, 100.5, True]

print(myList)
myList[0:3] = [55, "A", False]
myList[-1] = False
print(myList)


list = ["Ahmed", "Eslam", "Mossab"]
list.append("Hassan")
print(list)

Slist = ["Noor", "Mohamed", "Adam"]
list.append(Slist)
print(list)
print(list[4])
print(list[4][2])

a = [1, 2, 3, 4]
b = ["A", "B", "C", "D"]
a.extend(b)

print(a)
print(a[6])

d = [1, 2, 3, 4, 3, 9, 10, 1, 2, 1]
print(d.count(3))
print(d.index(10))
d.insert(-1, "Hello")
print(d)
