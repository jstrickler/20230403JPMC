from collections import defaultdict

junk = {
    'a': 5,
    'm': 18,
}
print(f"junk['a']: {junk['a']}")
# print(f"junk['spam']: {junk['spam']}")
print(f"junk.get('spam', 0): {junk.get('spam', 0)}")

def zero():
    return 0

junk = defaultdict(zero)
junk = defaultdict(lambda: 0)  # same

junk['a'] = 5
junk['m'] = 18
print(f"junk: {junk}")
print(f"junk['spam']: {junk['spam']}")


fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

fruit_dict = defaultdict(list)
for fruit in fruits:
    first = fruit[0]
    fruit_dict[first].append(fruit)
print(f"fruit_dict: {fruit_dict}")


for letter, fruit_list in sorted(fruit_dict.items()):
    print(letter, fruit_list)
print()


