class Milk:
    def __init__(self, liters: float, price_per_liter: int):
        self.liters = liters
        self.price_per_liter = price_per_liter


class Sugar:
    def __init__(self, kg: float, price_per_kg: int):
        self.kg = kg
        self.price_per_kg = price_per_kg


class Recipe:
    def __init__(self, milk_ratio: float, sugar_ratio: float):
        self.milk_ratio = milk_ratio  # retseptdagi sut miqdori
        self.sugar_ratio = sugar_ratio  # retseptdagi shakar miqdori


class Piece:
    def __init__(self, weight: float, price: int):
        self.weight = weight  # bitta muzqaymoq og'irligi (kg)
        self.price = price  # bitta muzqaymoq narxi


class IceCream:
    def __init__(self, recipe: Recipe, piece: Piece):
        self.recipe = recipe
        self.piece = piece
        self.milk_available = 0.0  # mavjud sut (litr)
        self.sugar_available = 0.0  # mavjud shakar (kg)
        self.balance = 0  # umumiy pul
        self.sales = []  # sotilgan muzqaymoqlar ro'yhati

    def add_milk(self, milk: Milk):
        """Sut qo'shish"""
        self.milk_available += milk.liters

    def add_sugar(self, sugar: Sugar):
        """Shakar qo'shish"""
        self.sugar_available += sugar.kg

    def get_count(self) -> int:
        """Tayyorlash mumkin bo‘lgan muzqaymoqlar soni"""
        # Sut va shakar nisbati retseptga qarab
        milk_based = self.milk_available // self.recipe.milk_ratio
        sugar_based = self.sugar_available // self.recipe.sugar_ratio
        return int(min(milk_based, sugar_based))

    def buy(self, count: int) -> bool:
        """Muzqaymoq sotish"""
        available = self.get_count()
        if count > available:
            return False  # yetarli ingredient yo'q
        # ingredientlarni kamaytirish
        self.milk_available -= count * self.recipe.milk_ratio
        self.sugar_available -= count * self.recipe.sugar_ratio
        total_price = count * self.piece.price
        self.balance += total_price
        self.sales.append(f"{count}x{self.piece.price}={total_price}")
        return True

    def get_balance(self) -> int:
        """Joriy balans"""
        return self.balance

    def has_ice_cream(self) -> bool:
        """Muzqaymoq tayyorlash mumkinmi"""
        return self.get_count() > 0

    def get_info(self):
        """Sotilgan muzqaymoqlar ro'yhati"""
        return "\n".join(self.sales)

    def get_profit(self) -> int:
        """Umumiy foyda"""
        return self.balance


# ===== Misol ishlatish =====
if __name__ == "__main__":
    milk = Milk(80, 2000)  # 80 litr sut, 1L narxi 2000
    sugar = Sugar(120, 6000)  # 120 kg shakar, 1kg narxi 6000
    recipe = Recipe(2, 1)  # retsept: 2L sut, 1kg shakar
    piece = Piece(0.2, 2000)  # 0.2kg muzqaymoq, 2000 narxi

    ic = IceCream(recipe, piece)
    ic.add_milk(milk)
    ic.add_sugar(sugar)

    print("Tayyorlash mumkin bo'lgan muzqaymoqlar:", ic.get_count())
    print("Sotish:", ic.buy(5))  # 5 dona sotish
    print("Joriy balans:", ic.get_balance())
    print("Muzqaymoq tayyorlash mumkinmi?", ic.has_ice_cream())
    print("Sotilgan muzqaymoqlar ro'yhati:\n", ic.get_info())
    print("Umumiy foyda:", ic.get_profit())
