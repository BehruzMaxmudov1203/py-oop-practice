class Convertor:
    # kursni class darajasida saqlaymiz, barcha obyektlar uchun bir xil bo'ladi
    rate = 10500  # 1 dollar = 10500 so'm (misol)

    def __init__(self):
        pass

    @classmethod
    def set_rate(cls, new_rate: float):
        """Kursni o'zgartirish (barcha obyektlarga ta'sir qiladi)."""
        cls.rate = new_rate

    @classmethod
    def get_sum(cls, dollar: float) -> float:
        """Dollarni so'mga aylantirish."""
        return dollar * cls.rate

    @classmethod
    def get_dollar(cls, som: float) -> float:
        """So'mni dollarga aylantirish."""
        return som / cls.rate


# ===== Misol ishlatish =====
if __name__ == "__main__":
    c1 = Convertor()
    print("1 dollar =", c1.get_sum(1), "so'm")  # 10500 so'm
    print("10500 so'm =", c1.get_dollar(10500), "dollar")  # 1 dollar

    Convertor.set_rate(11000)  # kursni yangilash
    print("1 dollar yangi kurs =", c1.get_sum(1), "so'm")  # 11000 so'm
