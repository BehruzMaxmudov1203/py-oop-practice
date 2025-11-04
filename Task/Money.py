class Money:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"{self.value} so'm"


class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.moneys = []

    def add(self, money):
        if self.isFull():
            print("❌ Quti to‘la! Pulni qo‘shib bo‘lmaydi.")
            return False
        self.moneys.append(money)
        print(f"✅ {money.value} so‘m qo‘shildi ({self.getMoneyCount()}/{self.capacity})")
        return True

    def isEmpty(self):
        return len(self.moneys) == 0

    def isFull(self):
        return len(self.moneys) >= self.capacity

    def getMoneyCount(self):
        return len(self.moneys)

    def getAmount(self):
        return sum(m.value for m in self.moneys)


# 🔹 Test
b = MoneyBox(3)
a1 = Money(500)
a2 = Money(1000)
a3 = Money(2000)
a4 = Money(500)

b.add(a1)
b.add(a2)
b.add(a3)
b.add(a4)
print("💰 Umumiy summa:", b.getAmount())
print("Bo‘sh:", b.isEmpty(), "| To‘la:", b.isFull())
