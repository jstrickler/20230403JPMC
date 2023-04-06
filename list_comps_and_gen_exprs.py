fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

#     [expr  for var in iterable]
f1 = [f.upper() for f in fruits]
print(f"f1: {f1}\n")

f2 = [f.title() for f in fruits if f.startswith('p')]
print(f"f2: {f2}\n")

f3 = [f for f in fruits if f.startswith('a')]
print(f"f3: {f3}\n")

f4 = [(f[0].upper(), len(f)) for f in fruits]
print(f"f4: {f4}\n")

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

dobs = [p[-1] for p in people[-6:] if p[-1] > '1970']
print(f"dobs: {dobs}\n")

dobs_gen = ((p[0], p[1], p[-1]) for p in people[-6:] if p[-1] < '1970')
print(f"dobs_gen: {dobs_gen}\n")
for dob in dobs_gen:
    print(dob)
print()

f_gen = (f.upper() for f in fruits if len(f) > 6)
for fruit in f_gen:
    print(fruit)
print()

with open('my_huge_gigabyte_file.txt') as gig_in:
    with open('my_huge_local_file.txt', 'w') as gig_out:
        for raw_line in gig_in:
            line = raw_line.rstrip()
            # process line here ???
            gig_out.write(line)






