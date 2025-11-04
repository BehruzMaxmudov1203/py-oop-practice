from abc import ABC, abstractmethod

class AbstractA(ABC):
    @abstractmethod
    def get_age(self):
        pass

    def __eq__(self, other):
        if isinstance(other, AbstractA):
            return self.get_age() == other.get_age()
        return False


class ClassB(AbstractA):
    def __init__(self, age):
        self.age = age

    def get_age(self):
        return self.age


# Test
b1 = ClassB(25)
b2 = ClassB(25)
b3 = ClassB(30)
print("b1 == b2:", b1 == b2)
print("b1 == b3:", b1 == b3)
