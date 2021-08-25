# Dictionary
from typing import Mapping
user = {
    "name": "Ahmed",
    "age": 25,
    "country": "Egypt",
    "skills": ["html", "css", "JS"],
    "rating": 10.5
}

print(user)
print(user["country"])
print(user.get("age"))

print(user.keys())
print(user.values())

languages = {
    "one": {
        "name": "Html",
        "progress": "80%"
    },
    "two": {
        "name": "css",
        "progress": "90%"
    },
    "Three": {
        "name": "Js",
        "progress": "90%"
    }

}

print(languages)
print(languages["one"])
print(languages["Three"]["name"])

print(len(languages))
print(len(languages["two"]))

frameworkOne = {
    "name": "Vuejs",
    "progress": " 80%"}
frameworkTwo = {
    "name": "Reactjs",
    "progress": " 80%"
}
frameworkThree = {
    "name": "Angular",
    "progress": " 80%"
}

allframework = {
    "one": frameworkOne,
    "two": frameworkTwo,
    "three": frameworkThree
}
print(allframework)


# Clear


user = {
    "name": " Ahmed"
}
print(user)
user.clear()
print(user)

print("=" * 50)

# Update

member = {
    "name": "Ahmed"
}
print(member)
member["Age"] = 25
print(member)
member.update({"country": "Egypt"})
print(member)

print("=" * 50)

# Copy
main = {
    "name": "Ahmed"
}
b = main.copy()
print(b)
main.update({"country": "Egypt"})
print(b)
print(main)
print("=" * 50)

# keys()    +  value()
print(main.keys())
print(main.values())


# setdefault ()
user = {
    "name": "Osama"
}
print(user)
print(user.setdefault("Age", 25))
print(user)

print("=" * 50)

# popitem()

member = {
    "name": "Osama",
    "skill": " PS4"
}
print(member)
member.update({"age": 30})
print(member.popitem())

print("=" * 50)

# Items
view = {
    "name": "Osama",
    "Skill": "XBox"
}

allItems = view.items()
print(view)
view["age"] = 36
print(allItems)

print("="*50)

# fromkeys()

a = ('MyKeyOne', 'MyKeyTwo', 'MyKeyThree')
b = "X"
print(dict.fromkeys(a, b))
