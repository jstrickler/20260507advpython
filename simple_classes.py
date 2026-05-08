from datetime import date

cities = list()

# instance = class(...)

cities.append("Bournemouth")
cities.append("Pune")
cities.append("Jersey City")
cities.append("Columbus")

cities.insert(0, "Durham")
print(f"{cities = }\n")

class Dog:
    def bark(self):
        print("Woof! woof!")

d1 = Dog()
d2 = Dog()
d1.bark()
d2.bark()

d = date(2026, 1, 1)
print(f"{d = }\n")
print(f"{d.year = }")





