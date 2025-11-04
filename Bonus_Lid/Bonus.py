# 1️⃣ Lid sinfi - qopqoqdagi kodni saqlaydi
class Lid:
    def __init__(self, code: str):
        self.code = code  # 8 xonali qopqoq kodi


# 2️⃣ Bonus sinfi - yutuqlar sonini boshqaradi
class Bonus:
    def __init__(self, count: int):
        self.remaining = count  # yutuqlar soni qolgan

    @staticmethod
    def char_value(ch: str) -> int:
        """
        Belgining qiymatini hisoblash:
        a,A=1, b,B=2, ..., z,Z=26, 1-9=1-9
        """
        if ch.isalpha():  # harf bo'lsa
            return ord(ch.lower()) - ord('a') + 1
        elif ch.isdigit():  # raqam bo'lsa
            return int(ch)
        else:
            return 0  # boshqa belgilarni 0 deb olamiz

    @staticmethod
    def is_valid_lid_code(code: str) -> bool:
        """Kod shartlariga mosligini tekshirish"""
        if len(code) != 8:
            return False

        first4_sum = sum(Bonus.char_value(ch) for ch in code[:4])
        last4_sum = sum(Bonus.char_value(ch) for ch in code[4:])

        # Unlilar va undoshlar sonini tengligini tekshirish
        vowels = "aeiouAEIOU"
        vowels_count = sum(1 for ch in code if ch in vowels)
        consonants_count = sum(1 for ch in code if ch.isalpha() and ch not in vowels)

        return first4_sum == last4_sum and vowels_count == consonants_count

    def check(self, lid: Lid) -> bool:
        """Yutuqli qopqoqni tekshirish"""
        if self.remaining <= 0:
            print("Yutuqlar tugagan, qopqoq yutqazildi.")
            return False
        if self.is_valid_lid_code(lid.code):
            self.remaining -= 1
            print(f"{lid.code} yutuqli qopqoq! Qolgan yutuqlar: {self.remaining}")
            return True
        else:
            print(f"{lid.code} yutuqli emas.")
            return False


# ===== Misol ishlatish =====
if __name__ == "__main__":
    bonus = Bonus(4)
    lid1 = Lid("abaa2334")
    lid2 = Lid("abA12BBA")
    lid3 = Lid("abaa2334")

    print(bonus.check(lid1))  # True/False
    print(bonus.check(lid2))  # True/False
    print(bonus.check(lid3))  # True/False
