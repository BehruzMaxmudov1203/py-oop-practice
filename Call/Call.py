class Client:
    def __init__(self, callPrice, smsPrice):
        self.callPrice = callPrice      # 1 daqiqa qo'ng'iroq narxi
        self.smsPrice = smsPrice        # 1 ta SMS narxi
        self.balance = 0                # Hisobdagi pul

    # Hisobga pul qo'shish
    def addSum(self, amount):
        self.balance += amount
        print(f"{amount} so'm qo'shildi. Joriy balans: {self.balance} so'm")

    # Hisob aktivligini tekshirish
    def isActive(self):
        is_active = self.balance > 0
        print(f"Hisob aktiv: {is_active}")
        return is_active

    # Qo'ng'iroq qilish funksiyasi
    def call(self, minutes):
        cost = minutes * self.callPrice
        if self.balance >= cost:
            self.balance -= cost
            print(f"{minutes} daqiqa qo'ng'iroq qilindi. {cost} so'm yechildi. Qoldiq: {self.balance} so'm")
            return True
        else:
            print("Balans yetarli emas! Qo'ng'iroq amalga oshmadi.")
            return False

    # SMS yuborish funksiyasi
    def sms(self, count):
        cost = count * self.smsPrice
        if self.balance >= cost:
            self.balance -= cost
            print(f"{count} ta SMS yuborildi. {cost} so'm yechildi. Qoldiq: {self.balance} so'm")
            return True
        else:
            print("Balans yetarli emas! SMS yuborilmadi.")
            return False


# ==== Dasturni tekshirish ====
a = Client(100, 200)  # 1 daqiqa = 100 so'm, 1 SMS = 200 so'm
a.addSum(2000)
a.addSum(1500)
a.isActive()
a.call(4)
a.sms(3)
a.call(2)
