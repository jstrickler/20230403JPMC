from collections import namedtuple
from dataclasses import dataclass

name = "Jack", "Ryan"
print(f"name: {name}")
print(name[0], name[1])

Name = namedtuple('Name', "first_name last_name")


j = Name("Jack", "Ryan")
print(f"j: {j}")
print(f"j.first_name: {j.first_name}")
print(f"j.last_name: {j.last_name}")
print(Name.__name__)

def spam(name: Name) -> list:
    pass

#  dataclasses

@dataclass
class Name:
    first_name: str
    last_name: str

n = Name(first_name="Jack", last_name="Sprat")
print(f"n: {n}")
print(n.first_name, n.last_name)
n.first_name = "Sallie"
print(f"n: {n}")

