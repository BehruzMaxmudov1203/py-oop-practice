import random

class User:
    def __init__(self, first_name: str, last_name: str, age: int, phone_number: str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone_number = phone_number


class Telegram:
    def __init__(self):
        self.accounts = {}  # {phone_number: User}
        self.sms_codes = {}  # {phone_number: code}

    def create_account(self, user: User) -> bool:
        """
        User profil mavjud bo'lmasa SMS code yuboradi va True qaytaradi.
        Profil mavjud bo'lsa False qaytaradi.
        """
        if user.phone_number in self.accounts:
            return False
        # 4 xonali SMS code yaratish
        code = random.randint(1000, 9999)
        self.sms_codes[user.phone_number] = code
        print(f"SMS code sent to {user.phone_number}: {code}")  # demo uchun print
        return True

    def check_sms_code(self, code: int, phone_number: str) -> bool:
        """
        Telefon va code mos kelsa account yaratadi.
        Aks holda xatolik xabar beradi.
        """
        if phone_number in self.sms_codes and self.sms_codes[phone_number] == code:
            # SMS code to'g'ri, account yaratish
            del self.sms_codes[phone_number]
            print(f"Account created for {phone_number}")
            return True
        print(f"Error: Incorrect code for {phone_number}")
        return False

    def get_user_count(self) -> int:
        """Hozirda mavjud bo‘lgan accountlar soni"""
        return len(self.accounts)

    def delete_account(self, phone_number: str) -> bool:
        """
        Ko‘rsatilgan telefon raqamli user mavjud bo‘lsa, accountni o‘chiradi.
        Aks holda False qaytaradi.
        """
        if phone_number in self.accounts:
            del self.accounts[phone_number]
            print(f"Account with {phone_number} deleted.")
            return True
        print(f"No account with {phone_number} found.")
        return False
