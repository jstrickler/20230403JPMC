from itertools import islice, chain

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

ufruits = (f.upper() for f in fruits)

print(f"ufruits: {ufruits}\n")

# print(f"ufruits[:4]: {ufruits[:4]}\n")
result = islice(ufruits, 0, 4) 
print(f"result: {result}\n")
print(f"list(result): {list(result)}\n")

pile1 = ['a', 'b', 'c']
pile2 = 'd', 'e', 'f'
d = {'foo': 88, 'bar': 26}

for value in chain(pile1, pile2, d.items()):
    print(value)
print('-' * 60)

pile3 = [[1, 2, 3], [[1,2],[3,4]], ['foo', 'bar', 'blah'], (4, 5, 6), "abc", [7, 8, 9, 10]]
for value in chain.from_iterable(pile3):
    print(value)

