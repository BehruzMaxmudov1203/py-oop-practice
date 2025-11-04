class Contact:
    def __init__(self, name, number, imgUrl):
        self.name = name
        self.number = number
        self.imgUrl = imgUrl

    def show(self):
        print(f"Ismi: {self.name}")
        print(f"Telefon raqami: {self.number}")
        print(f"Rasm manzili: {self.imgUrl}")



contact1 = Contact("Ali", "+998901234567", "https://example.com/ali.jpg")
contact1.show()
