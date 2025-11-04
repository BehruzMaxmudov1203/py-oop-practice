class Ingredient:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __repr__(self):
        return f"{self.name} ({self.amount})"


# Misol uchun ba'zi mahsulotlar:
class Apple(Ingredient):
    def __init__(self, amount):
        super().__init__("Olma", amount)


class Sugar(Ingredient):
    def __init__(self, amount):
        super().__init__("Shakar", amount)


class Flour(Ingredient):
    def __init__(self, amount):
        super().__init__("Un", amount)


# Receipt (retsept)
class Receipt:
    def __init__(self):
        self.ingredients = {}  # ingredient: kerakli miqdor
        self.capacity = 20

    def addIngredient(self, ingredient, count):
        if len(self.ingredients) >= self.capacity:
            print("❌ Retsept to‘la!")
            return False
        self.ingredients[ingredient.name] = count
        print(f"✅ {ingredient.name} ({count} dona) retseptga qo‘shildi.")
        return True

    def isFull(self):
        return len(self.ingredients) >= self.capacity

    def isEmpty(self):
        return len(self.ingredients) == 0

    def show(self):
        print("📋 Retsept:")
        for k, v in self.ingredients.items():
            print(f" - {k}: {v} dona kerak")


# Food sinfi
class Food:
    def __init__(self, receipt):
        self.receipt = receipt
        self.stock = {}

    def add(self, ingredient):
        self.stock[ingredient.name] = self.stock.get(ingredient.name, 0) + ingredient.amount
        print(f"➕ {ingredient.amount} ta {ingredient.name} qo‘shildi")

    def getCount(self):
        possible = []
        for name, needed in self.receipt.ingredients.items():
            have = self.stock.get(name, 0)
            possible.append(have // needed)
        return min(possible) if possible else 0

    def hasFood(self):
        return self.getCount() > 0

    def getReceipt(self):
        return self.receipt


# 🔹 Test
apple = Apple(5)
sugar = Sugar(10)
flour = Flour(6)

r = Receipt()
r.addIngredient(apple, 3)
r.addIngredient(sugar, 5)
r.addIngredient(flour, 2)
r.show()

f = Food(r)
f.add(Apple(6))
f.add(Sugar(10))
f.add(Flour(4))

print("🍎 Tayyor bo‘ladigan taomlar soni:", f.getCount())
print("Tayyor bo‘lish mumkinmi?", f.hasFood())
