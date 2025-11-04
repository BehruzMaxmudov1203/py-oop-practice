# 1️⃣ Meva sinfi
class Fruit:
    def __init__(self, name: str, color: str, weight: float):
        self.name = name
        self.color = color
        self.weight = weight  # kg

    def show(self):
        """Meva haqida ma'lumot chiqarish"""
        print(f"Meva: {self.name}, Rang: {self.color}, Og'irligi: {self.weight} kg")




# ===== Misol ishlatish =====
if __name__ == "__main__":
    f = Fruit("Olma", "Qizil", 0.25)
    f.show()

