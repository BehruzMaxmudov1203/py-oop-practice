class Capacity:
    def __init__(self, capacity: int):
        self.capacity = capacity  # Maksimal yoqilg'i miqdori


class Oil:
    def __init__(self, amount: int):
        self.amount = amount  # Yo'qilg'i hajmi


class Outgoing:
    def __init__(self, distance: int, oil_needed: int):
        self.distance = distance  # Masofa
        self.oil_needed = oil_needed  # Masofa uchun yoqilg'i sarfi


class Direction:
    def __init__(self, distance: int):
        self.distance = distance  # Masofa (km)


class Car:
    def __init__(self, outgoing: Outgoing, capacity: Capacity):
        self.outgoing = outgoing
        self.capacity = capacity
        self.current_oil = 0  # Joriy yoqilg'i miqdori

    def go(self, direction: Direction) -> bool:
        """Berilgan masofaga borishga urinadi"""
        if self.current_oil >= direction.distance:
            self.current_oil -= direction.distance
            return True
        return False

    def add_oil(self, oil: Oil) -> bool:
        """Yoqilg'i qo'shadi"""
        if self.current_oil + oil.amount <= self.capacity.capacity:
            self.current_oil += oil.amount
            return True
        return False

    def is_full_oil(self) -> bool:
        """Yoqilg'i to'la ekanini tekshiradi"""
        return self.current_oil >= self.capacity.capacity

    def has_oil(self) -> bool:
        """Yoqilg'i mavjudligini tekshiradi"""
        return self.current_oil > 0

    def get_max_direction(self) -> int:
        """Mavjud yoqilg'i bilan qancha km yura olish mumkinligini qaytaradi"""
        return self.current_oil
