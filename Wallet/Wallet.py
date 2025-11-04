from typing import List

class Card:
    def __init__(self, username: str, card_number: str, amount: int):
        self.username = username
        self.card_number = card_number
        self.amount = amount

    def __str__(self):
        """Card ma’lumotlarini chiqarish"""
        return f"Card(username={self.username}, number={self.card_number}, amount={self.amount})"


class ShowCardInterface:
    """Kartalarni ko‘rsatish uchun interface"""
    def show_card_data(self, card: Card):
        raise NotImplementedError


class LogInterface:
    """Xabar berish uchun interface"""
    def send_message(self, message: str):
        raise NotImplementedError


class Wallet:
    def __init__(self):
        self.cards: List[Card] = []
        self.cash_balance: int = 0
        self.card_listener: ShowCardInterface = None
        self.log_listener: LogInterface = None

    def set_show_card_interface(self, card_listener: ShowCardInterface):
        self.card_listener = card_listener

    def set_log_interface(self, log_listener: LogInterface):
        self.log_listener = log_listener

    def add_card(self, card: Card):
        """Yagona karta qo‘shish"""
        if any(c.card_number == card.card_number for c in self.cards):
            if self.log_listener:
                self.log_listener.send_message(f"Karta {card.card_number} allaqachon mavjud!")
            return
        self.cards.append(card)

    def add_cards(self, cards: List[Card]):
        """Bir nechta kartalarni qo‘shish"""
        for card in cards:
            if any(c.card_number == card.card_number for c in self.cards):
                if self.card_listener:
                    self.card_listener.show_card_data(card)
            else:
                self.cards.append(card)

    def add_balance(self, add_balance: int):
        """Naxt pul qo‘shish"""
        self.cash_balance += add_balance

    def get_total_balance(self) -> int:
        """Hamyondagi joriy balans"""
        return self.cash_balance + sum(c.amount for c in self.cards)

    def get_all_cards(self):
        """Hamyon kartalarini ko‘rsatish"""
        if self.card_listener:
            for c in self.cards:
                self.card_listener.show_card_data(c)

    def spend_money(self, money: int):
        """Naxt puldan xarajat qilish"""
        if money <= self.cash_balance:
            self.cash_balance -= money
        else:
            deficit = money - self.cash_balance
            if self.log_listener:
                self.log_listener.send_message(f"Yetarli pul yo‘q! Yetmayotgan summa: {deficit}")

    def spend_money_from_card(self, card: Card, spend_money: int):
        """Card orqali xarajat qilish"""
        target_card = next((c for c in self.cards if c.card_number == card.card_number), None)
        if not target_card:
            if self.log_listener:
                self.log_listener.send_message(f"Karta topilmadi: {card.card_number}")
            return
        if spend_money <= target_card.amount:
            target_card.amount -= spend_money
        else:
            deficit = spend_money - target_card.amount
            if self.log_listener:
                self.log_listener.send_message(f"Karta yetarli pulga ega emas! Yetmayotgan summa: {deficit}")


# ===== Misol ishlatish =====
class CardPrinter(ShowCardInterface):
    def show_card_data(self, card: Card):
        print(f"Card Info: {card}")


class Logger(LogInterface):
    def send_message(self, message: str):
        print(f"LOG: {message}")


if __name__ == "__main__":
    wallet = Wallet()
    wallet.set_card_interface = CardPrinter()
    wallet.set_log_interface(Logger())

    # Kartalar
    card1 = Card("Alice", "1234", 5000)
    card2 = Card("Bob", "5678", 3000)
    card3 = Card("Alice", "1234", 2000)  # allaqachon mavjud

    # Add karta
    wallet.add_card(card1)
    wallet.add_card(card2)
    wallet.add_card(card3)  # log chiqadi

    # Naxt pul qo‘shish va xarajat
    wallet.add_balance(1000)
    wallet.spend_money(500)  # muvaffaqiyatli
    wallet.spend_money(2000)  # yetarli emas, log chiqadi

    # Card orqali xarajat
    wallet.spend_money_from_card(card1, 2000)
    wallet.spend_money_from_card(card2, 4000)  # yetarli emas, log chiqadi
