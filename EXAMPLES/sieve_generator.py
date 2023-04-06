
def next_prime(limit):
    flags = set()  # initialize empty set (to be used for "is-prime" flags

    for i in range(2, limit):
        if i in flags:
            continue
        for j in range(2 * i, limit + 1, i):
            flags.add(j)  # add non-prime elements to set
        # __next__()
        yield i  # execution stops here until next value is requested by for-in loop


np = next_prime(200)  # next_prime() returns a generator object
print(f"type(np): {type(np)}")

for prime in np:  # iterate over yielded primes
    print(prime, end=' ')
print()

def rainbow_gen():
    yield 'violet'
    yield 'blue'
    yield 'yellow'
    yield 'red'

g = rainbow_gen()

print(f"next(g): {next(g)}")
print(f"next(g): {next(g)}")
print(f"next(g): {next(g)}")
print(f"next(g): {next(g)}")
# print(f"next(g): {next(g)}")
print()

g2 = rainbow_gen()
for color in g2:
    print(color)

