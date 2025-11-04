import random
import re
from typing import List


class UserData:
    def __init__(self, name: str, age: int, phone_number: str):
        self.name = name
        self.age = age
        self.phone_number = phone_number

    def show_user_info(self):
        """Foydalanuvchi haqida ma’lumot chiqarish"""
        print(f"Name: {self.name}, Age: {self.age}, Phone: {self.phone_number}")


class LogInterface:
    """Xabar berish interface"""
    def show_message(self, message: str):
        raise NotImplementedError


class UserInfoInterface:
    """Foydalanuvchi ma’lumotini ko‘rsatish interface"""
    def show(self, user: UserData):
        raise NotImplementedError


class RegisterController:
    def __init__(self, max_users: int):
        self.max_users = max_users
        self.registered_users: List[UserData] = []
        self.log_listener: LogInterface = None
        self.user_listener: UserInfoInterface = None
        self.sms_codes = {}  # phone_number: code

    def set_log_interface(self, log_listener: LogInterface):
        self.log_listener = log_listener

    def set_user_info_interface(self, user_listener: UserInfoInterface):
        self.user_listener = user_listener

    def register(self, user: UserData):
        """User ro’yxatdan o’tkazish"""
        if user in self.registered_users:
            if self.log_listener:
                self.log_listener.show_message(f"{user.name} allaqachon ro'yxatdan o'tgan!")
            return False

        if len(self.registered_users) >= self.max_users:
            if self.log_listener:
                self.log_listener.show_message("Ro'yxat to'la!")
            return False

        # Ma’lumotlarni tekshirish
        return self.__check(user)

    def unregister(self, user: UserData):
        """Userni ro’yxatdan o‘chirish"""
        if user in self.registered_users:
            self.registered_users.remove(user)
        else:
            if self.log_listener:
                self.log_listener.show_message(f"{user.name} ro'yxatda mavjud emas!")

    # ===== Private methods =====
    def __check(self, user: UserData):
        """User ma’lumotlarini tekshirish"""
        # Name tekshirish: faqat lotin harflari va uzunligi 3-12
        if not re.fullmatch(r"[A-Za-z]{3,12}", user.name):
            if self.log_listener:
                self.log_listener.show_message(f"{user.name} ismi noto'g'ri!")
            return False

        # Age tekshirish
        if not (16 <= user.age <= 25):
            if self.log_listener:
                self.log_listener.show_message(f"{user.name} yoshi 16-25 oralig'ida bo'lishi kerak!")
            return False

        # Phone number tekshirish: 10-14 raqam
        if not re.fullmatch(r"\d{10,14}", user.phone_number):
            if self.log_listener:
                self.log_listener.show_message(f"{user.name} telefon raqami noto'g'ri!")
            return False

        # Agar barcha tekshiruvlardan o'tdi
        self.__send_sms_code(user.phone_number)
        return True

    def __send_sms_code(self, phone_number: str):
        """Telefon raqamga 4 xonali SMS code yuborish"""
        code = random.randint(1000, 9999)
        self.sms_codes[phone_number] = code
        if self.log_listener:
            self.log_listener.show_message(f"SMS yuborildi {phone_number} ga: {code}")

    def check_sms_code(self, code: int, phone_number: str):
        """Yuborilgan code tekshirish"""
        if phone_number in self.sms_codes and self.sms_codes[phone_number] == code:
            # Ro’yxatdan o‘tkazish
            user = next((u for u in self.registered_users if u.phone_number == phone_number), None)
            if user:
                self.registered_users.append(user)
            if self.log_listener:
                self.log_listener.show_message(f"{phone_number} muvaffaqiyatli tasdiqlandi!")
            return True
        else:
            if self.log_listener:
                self.log_listener.show_message(f"{phone_number} code noto'g'ri!")
            return False

    def repeat_send_sms_code(self, user: UserData):
        """Code qayta yuborish"""
        if user.phone_number in self.sms_codes:
            self.__send_sms_code(user.phone_number)
        else:
            if self.log_listener:
                self.log_listener.show_message(f"{user.name} uchun code mavjud emas!")

    def get_all_users(self):
        """Ro’yxatdan o’tgan userlarni ko‘rsatish"""
        if self.user_listener:
            for u in self.registered_users:
                self.user_listener.show(u)
