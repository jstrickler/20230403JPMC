from pprint import pprint
import mystuff
from mystuff import city
#print(f"mystuff.city: {mystuff.city}")
print(f"city: {city}\n")

animal = "wombat"  # global

class Kangaroo:
    pass

k = Kangaroo()

def spam(stuff):   # global
    def toast():
        pass
    class Foo:
        def yell(self):
            print("WHOO-HOOO Python is weird")
    word = "badger"   # local
    print(word * 3)
    print(f"locals(): {locals()}")
    return Foo()

c = spam(98)
c.yell()

spam(5)
print(f"animal: {animal}")

g = globals()
pprint(g)

x = g['Kangaroo']()
print(f"type(x): {type(x)}")

print(f"g['animal']: {g['animal']}")

g['spam'](123)

print(f"dir(mystuff): {dir(mystuff)}")

g['color'] = "blue"

print(f"color: {color}")

g['bark'] = lambda : print("woof woof")

bark()
