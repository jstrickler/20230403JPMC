from collections import defaultdict

fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

f0 = sorted(fruits)
print(f"f0: {f0}\n")

def ignore_case(s):
    return s.lower()

f1 = sorted(fruits, key=ignore_case)
print(f"f1: {f1}\n")

f2 = sorted(fruits, key=lambda s: s.lower())
print(f"f2: {f2}\n")

d = defaultdict(lambda: 0)

f3 = sorted(fruits, key=lambda f: (len(f), f.lower()), reverse=True)
print(f"f3: {f3}\n")

# silly:
x = lambda s: 2 * s
print(x(100))
print(x('ha'))