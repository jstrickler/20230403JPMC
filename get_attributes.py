from president import President

class GetAttributes:
    def __init__(self, *attrs):
        self._attrs = attrs

    def __call__(self, obj):
        # convert generator to tuple
        return tuple(getattr(obj, attr) for attr in self._attrs)

if __name__ == "__main__":

    class Spam:
        @property
        def first_name(self):
            return "Martin"
    
        @property
        def last_name(self):
            return "Guido"
    

    get_names = GetAttributes('first_name', 'last_name')

    sp = Spam()

    print(f"get_names(sp): {get_names(sp)}")

    p = President(1)
    
    def get_my_attributes():
        return get_names(p) + get_names(sp)
    
    print(f"get_my_attributes(): {get_my_attributes()}")

    print(f"get_names(p): {get_names(p)}")
    data = get_names(p)
    data =  p.first_name, p.last_name

    p = President(26)
    print(f"get_names(p): {get_names(p)}")
    print('-' * 60)

    get_party = GetAttributes('birth_state', 'party')
    print(f"get_party(President(3)): {get_party(President(3))}")
    print('-' * 60)

    get_info = GetAttributes('last_name', 'birth_state', 'party')
    info = [get_info(President(i)) for i in range(1,11)]
    print(f"info: {info}")
    print('-' * 60)

    # full disclosure -- such a thing already exists
    from operator import attrgetter

    get_info2 = attrgetter('last_name', 'birth_state', 'party')
    info2 = [get_info2(President(i)) for i in range(1,11)]
    print(f"info2: {info2}")

    