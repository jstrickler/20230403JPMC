from president import President
import typing as T

class GetAttributes:
    def __init__(self, *attrs: T.Iterable[str]):
        self.attrs = attrs

    def __call__(self, obj: T.Any) -> tuple:
        return tuple(getattr(obj, attr) for attr in self.attrs)

if __name__ == "__main__":
    
    get_names = GetAttributes('first_name', 'last_name')

    p = President(1)

    print(f"get_names(p): {get_names(p)}")

    print(get_names(p))

    p = President(26)
    print(f"get_names(p): {get_names(p)}")

    get_party = GetAttributes('birth_state', 'party')
    print(f"get_party(President(3)): {get_party(President(3))}")

    get_info = GetAttributes('last_name', 'birth_state', 'party')
    info = [get_info(President(i)) for i in range(1,11)]
    print(f"info: {info}")

    # full disclosure -- such a thing already exists
    from operator import attrgetter

    get_info2 = attrgetter('last_name', 'birth_state', 'party')
    info2 = [get_info2(President(i)) for i in range(1,11)]
    print(f"info2: {info2}")

    