class Money:
    def __init__(self, value):
        self.value = value  # pul qiymati (masalan: 1000, 5000)

    def __repr__(self):
        return f"{self.value} so'm"


# Moneybox sinfi — pul qutisi
class Moneybox:
    def __init__(self, capacity):
        self.capacity = capacity  # sig'im (nechta pul sig'adi)
        self.moneys = []          # ichidagi pullar ro'yxati

    # Pul qo‘shish
    def add(self, money):
        if self.isFull():
            print(f"❌ Quti to‘la! {money.value} so‘mlik pulni qo‘shib bo‘lmaydi.")
            return False
        self.moneys.append(money)
        print(f"✅ {money.value} so‘mlik pul qutiga qo‘shildi ({self.getMoneyCount()}/{self.capacity})")
        return True

    # Bo‘shlikni tekshirish
    def isEmpty(self):
        empty = len(self.moneys) == 0
        print(f"📭 Quti bo‘sh: {empty}")
        return empty

    # To‘lalikni tekshirish
    def isFull(self):
        full = len(self.moneys) >= self.capacity
        return full

    # Pullar sonini olish
    def getMoneyCount(self):
        return len(self.moneys)

    # Umumiy qiymatini olish
    def getAmount(self):
        total = sum(m.value for m in self.moneys)
        return total


# ==== Dastur tekshiruvi ====
print("💰 JAMG‘ARMA QUTISI TESTI\n")

# 5 ta pul sig‘adigan quti
box = Moneybox(5)

# Turli qiymatdagi pullar
m1 = Money(1000)
m2 = Money(5000)
m3 = Money(10000)
m4 = Money(2000)
m5 = Money(500)
m6 = Money(1000)  # ortiqcha pul (sig‘maydi)

# Pullarni qo‘shamiz
box.add(m1)
box.add(m2)
box.add(m3)
box.add(m4)
box.add(m5)
box.add(m6)   # bu sig‘maydi

# Holatlarni tekshiramiz
box.isEmpty()
print(f"💵 Pullar soni: {box.getMoneyCount()}")
print(f"💰 Umumiy summa: {box.getAmount()} so'm")
print(f"Quti to‘la: {box.isFull()}")
