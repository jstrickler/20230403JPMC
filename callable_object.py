
apple = 5

def banana():
    print("banana!")
    return "abc"

class Wombat:
    pass

for thing in apple, banana, Wombat:
    if callable(thing):
        print(thing())
    else:
        print(thing)

