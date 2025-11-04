class Ingredient:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

    def __repr__(self):
        return f"{self.name} ({self.volume}l)"


# Mahsulotlar (vorislar)
class Potato(Ingredient):
    def __init__(self, volume):
        super().__init__("Kartoshka", volume)


class Carrot(Ingredient):
    def __init__(self, volume):
        super().__init__("Sabzi", volume)


class Meat(Ingredient):
    def __init__(self, volume):
        super().__init__("Go‘sht", volume)


class Oil(Ingredient):
    def __init__(self, volume):
        super().__init__("Yog‘", volume)


class Water(Ingredient):
    def __init__(self, volume):
        super().__init__("Suv", volume)


# Qozon (Caldron)
class Caldron:
    def __init__(self, capacity):
        self.capacity = capacity
        self.ingredients = []

    def add(self, ingredient):
        if self.getUsedSpace() + ingredient.volume > self.capacity:
            print(f"❌ {ingredient.name} sig‘madi! Qozon to‘ldi.")
            return False
        self.ingredients.append(ingredient)
        print(f"✅ {ingredient.name} qo‘shildi ({self.getUsedSpace()}/{self.capacity} l)")
        return True

    def isEmpty(self):
        return len(self.ingredients) == 0

    def isFull(self):
        return self.getUsedSpace() >= self.capacity

    def showIngredients(self):
        print("🍲 Tarkib:", ", ".join(i.name for i in self.ingredients))

    def getUsedSpace(self):
        return sum(i.volume for i in self.ingredients)

    def getFreeSpace(self):
        return self.capacity - self.getUsedSpace()


# 🔹 Test
c = Caldron(10)
c.add(Potato(3))
c.add(Meat(4))
c.add(Oil(2))
c.add(Water(3))
c.showIngredients()
print("Bo‘sh joy:", c.getFreeSpace())
print("To‘la:", c.isFull())
