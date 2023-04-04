import typing as T

Numeric = T.Union[int, float]
print(f"Numeric: {Numeric}")

def doit(a: str, b: Numeric) -> T.Iterable[str]:
    print("all is good??")
    return 1, 2, 3

x = doit('abc', 123)
print(f"x: {x}")

doit(47, 8.3)

def foo(m: T.Any):
    pass
