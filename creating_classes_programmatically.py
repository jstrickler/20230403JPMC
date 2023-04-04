
class Animal:
    pass


def speak(self):
    print("woof! woof!")

Dog = type("Dog", (Animal,), {'bark': speak})

d = Dog()
d.bark()

print(f"type(d): {type(d)}")
print(f"Dog.__name__: {Dog.__name__}")
print(f"type(d).__name__: {type(d).__name__}")

