
file_obj = open('DATA/mary.txt')


function = 'read'
if hasattr(file_obj, function):
    reader = getattr(file_obj, function)
    if callable(reader):
        data = reader()
        print(f"data: {data}")
    else:
        raise TypeError("obj is not readable")

for attr in dir(file_obj):
    attr_value = getattr(file_obj, attr)
    print(attr, type(attr_value))

class Dog:
    def bark(self):
        print("Yip Yip")

d = Dog()

def bark(self):
    self._thing
    print("Woof! Woof!")

d.bark()

setattr(Dog, 'bark', bark)
x = list()

d.bark(x)

#  getattr() hasattr() setattr() delattr()

delattr(Dog, 'bark')

# d.bark()   this dog can't bark now








