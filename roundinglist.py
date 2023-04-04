
class RoundingList(list):
    def __setitem__(self, index, value):
        if isinstance(value, (int, float)):
            print("inserting")
            super().__setitem__(index, round(value, 2))
        else:
            raise TypeError("Rounding list only accepts numbers")

    def append(self, value):
        if isinstance(value, (int, float)):
            print("appending")
            super().append(round(value, 2))
        else:
            raise TypeError("Rounding list only accepts numbers")

r1 = RoundingList()
r1.append(5.3203920392)
print(f"r1: {r1}\n")
r1[0] = 20.473497394
print(f"r1: {r1}\n")
# r1[0] = "abc"
r1.append(35.32893824984)
# r1.append('abc')
print(f"r1: {r1}")
