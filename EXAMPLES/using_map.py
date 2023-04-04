#

strings = ['wombat', 'koala', 'kookaburra', 'blue-ringed octopus']

result = [s.upper() for s in strings]  # Using a list comprehension, which is usually simpler than map()
print(result)

result = map(str.upper, strings)
print(result)
print(list(result))

result = list(map(len, strings))  # Using map to get list of string lengths
print(result)

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

roots = map(lambda n: n ** .5, nums)
print(list(roots))

roots = [n ** .5 for n in nums]
print(f"roots: {roots}")

