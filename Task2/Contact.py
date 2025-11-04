class Contact:
    def __init__(self, name: str, number: str, email: str, address: str, favourite: bool):
        self.name = name
        self.number = number
        self.email = email
        self.address = address
        self.favourite = favourite

    def show(self):
        """Kontakt haqida ma'lumot chiqarish"""
        print(f"Ism: {self.name}")
        print(f"Telefon: {self.number}")
        print(f"Email: {self.email}")
        print(f"Manzil: {self.address}")
        print(f"Sevimli: {'Ha' if self.favourite else 'Yo‘q'}")


if __name__ == "__main__":

    c = Contact("Ali", "+998901234567", "ali@mail.com", "Toshkent", True)
    c.show()
