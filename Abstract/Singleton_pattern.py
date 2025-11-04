class SingletonA:
    __instance = None

    def __init__(self):
        if SingletonA.__instance is not None:
            raise Exception("Only one instance allowed!")
        else:
            SingletonA.__instance = self
            print("SingletonA instance created")

    @staticmethod
    def get_instance():
        if SingletonA.__instance is None:
            SingletonA()
        return SingletonA.__instance


# Test
a1 = SingletonA.get_instance()
a2 = SingletonA.get_instance()
print("a1 is a2:", a1 is a2)
