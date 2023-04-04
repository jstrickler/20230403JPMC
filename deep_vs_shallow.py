from copy import deepcopy

x = 5
print(f"x: {x}")
y = x
# z = 5
print(f"x: {x}")
print(f"y: {y}")
x = 10
print(f"x: {x}")
print(f"y: {y}")
z = 5  # uses existing object
print(id(y), id(z))
print(f"y is z: {y is z}")

colors = ['red', 'blue', 'purple']
colors.append('green')
print(f"colors: {colors}")
print('-' * 60)
c2 = colors  # (alias) does not make a copy
colors.append('pink')
print(f"colors: {colors}")
print(f"c2: {c2}")
colors.append(['spam', 'ham'])
print(f"colors: {colors}")

c3 = list(colors)  # shallow copy
c4 = colors[:]     # also shallow copy
print(id(colors), id(c2), id(c3), id(c4))
c3[-1].append('toast')
print(f"colors: {colors}")
print(f"c3: {c3}")
print('-' * 60)
c5 = deepcopy(colors)
c5[-1].append('waffles')
print(f"colors: {colors}")
print(f"c5: {c5}")

fruits = ['apple', 'cherry', 'date', 'tamarind']
x = fruits

def doit(data):
    for item in data:
        print(item.upper())
    data.append('banana')

doit(fruits)
print(f"fruits: {fruits}")







