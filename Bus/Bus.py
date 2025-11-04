class Capacity:
    def __init__(self, value):
        self.value = value  # Avtobus sig‘imi (nechta yo‘lovchi sig‘adi)


# Ticket (Chiptа) sinfi
class Ticket:
    def __init__(self, price):
        self.price = price  # Chipta narxi (so‘mda)


# Bus (Avtobus) sinfi
class Bus:
    def __init__(self, capacity, ticket):
        self.capacity = capacity.value      # Sig‘im
        self.ticket_price = ticket.price    # Chipta narxi
        self.current_passengers = 0         # Hozirgi yo‘lovchilar soni
        self.balance = 0                    # Avtobusdagi umumiy tushum (so‘mda)

    # Yo‘lovchilarni avtobusga chiqarish
    def inPassenger(self, count):
        """Avtobusga chiqmoqchi bo‘lgan yo‘lovchilar sonini qabul qiladi.
        Qancha sig‘gan bo‘lsa shuncha chiqadi va chiqganlar sonini qaytaradi."""
        available_seats = self.capacity - self.current_passengers

        if available_seats <= 0:
            print("❌ Avtobus to‘lgan! Hech kim chiqolmaydi.")
            return 0

        # Faqat sig‘ganini chiqaramiz
        added = min(count, available_seats)
        self.current_passengers += added
        self.balance += added * self.ticket_price
        print(f"🚍 {added} ta yo‘lovchi avtobusga chiqdi. Hozirgi yo‘lovchilar: {self.current_passengers}/{self.capacity}")
        return added

    # Yo‘lovchilarni avtobusdan tushurish
    def outPassenger(self, count):
        """Avtobusdan tushayotgan yo‘lovchilar sonini qabul qiladi.
        Qancha mavjud bo‘lsa shuncha tushadi va tushganlar sonini qaytaradi."""
        if self.current_passengers == 0:
            print("⚠️ Avtobusda yo‘lovchi yo‘q.")
            return 0

        removed = min(count, self.current_passengers)
        self.current_passengers -= removed
        print(f"🚶‍♂️ {removed} ta yo‘lovchi avtobusdan tushdi. Qoldi: {self.current_passengers}")
        return removed

    # Avtobusdagi pul miqdorini qaytarish
    def getBalance(self):
        print(f"💰 Avtobusdagi umumiy tushum: {self.balance} so‘m")
        return self.balance

    # Avtobus to‘lganligini tekshirish
    def isFull(self):
        full = self.current_passengers >= self.capacity
        print(f"🚌 Avtobus to‘lgan: {full}")
        return full

    # Avtobus bo‘shligini tekshirish
    def isEmpty(self):
        empty = self.current_passengers == 0
        print(f"🪑 Avtobus bo‘sh: {empty}")
        return empty


# ==== Dasturni tekshirish ====
cap = Capacity(10)     # Avtobusda 10 o‘rin
ticket = Ticket(2000)  # Har bir chipta 2000 so‘m
bus = Bus(cap, ticket)

bus.inPassenger(5)     # 5 ta yo‘lovchi chiqadi
bus.inPassenger(7)     # 5 sig‘gan, 2 ortiqcha
bus.isFull()           # To‘lganligini tekshiradi
bus.outPassenger(3)    # 3 ta tushadi
bus.isEmpty()          # Bo‘shligini tekshiradi
bus.getBalance()       # Tushumni ko‘rsatadi
