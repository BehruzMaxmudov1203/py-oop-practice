class ClassA:
    def __init__(self, value):
        self.__number = value   # private field

    # protected method
    def _get_number(self):
        return self.__number


class ClassB(ClassA):
    # make protected method public
    def get_number(self):
        return self._get_number()


# Test
b = ClassB(42)
print("ClassB number:", b.get_number())
