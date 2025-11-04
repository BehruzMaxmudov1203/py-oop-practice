class Thing:
    def __init__(self, name, volume):
        self.name = name        # Narsa nomi
        self.volume = volume    # Narsa hajmi


# Box (Quti) sinfi
class Box:
    def __init__(self, capacity):
        self.capacity = capacity    # Qutining umumiy sig‘imi
        self.current_volume = 0     # Hozircha band bo‘lgan hajm
        self.items = []             # Qutidagi narsalar ro‘yxati

    def push(self, thing):
        if self.current_volume + thing.volume <= self.capacity:
            self.items.append(thing)
            self.current_volume += thing.volume
            return True   # Muvaffaqiyatli joylashtirildi
        else:
            return False  # Joy yetmadi

    # isFull metodi — quti to‘lganligini tekshiradi
    def isFull(self):
        return self.current_volume >= self.capacity


# === Dasturni tekshirish ===
thing1 = Thing("Cola", 2)
thing2 = Thing("Chips", 1)
thing3 = Thing("Bread", 2)

box = Box(4)

print(box.push(thing1))  # True
print(box.push(thing2))  # True
print(box.push(thing3))  # False (sig‘imdan oshib ketadi)
print(box.isFull())      # True (to‘lgan)
