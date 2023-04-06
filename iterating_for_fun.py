
nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

inums = iter(nums)   #   nums.__iter__()
print(f"next(nums): {next(inums)}")
print(f"next(nums): {next(inums)}")
print(f"next(nums): {next(inums)}")

with open('DATA/mary.txt') as mary_in:
    print(f"type(mary_in): {type(mary_in)}")
    print(f"next(mary_in): {next(mary_in)}")   #  mary_in.__next__()
    print(f"next(mary_in): {next(mary_in)}")
    print(f"next(mary_in): {next(mary_in)}")
    print(f"next(mary_in): {next(mary_in)}")
#     print(f"next(mary_in): {next(mary_in)}")

with open('DATA/mary.txt') as mary_in:
    for line in mary_in:
        print(line)
print('-' * 60)


with open('DATA/knights.txt') as knights_in:
    header = next(knights_in)
    print(f"header: {header}")
    for raw_line in knights_in:
        line = raw_line.rstrip() # remove \n
        print(line)