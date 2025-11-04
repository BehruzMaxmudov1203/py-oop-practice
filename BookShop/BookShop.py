class Book:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name} ({self.price} so'm)"


class BookShop:
    def __init__(self, name, money):
        self.name = name
        self.total_money = money  # do'konga ajratilgan pul
        self.books = {}           # kitob: soni

    # yangi kitob sotib olish
    def buyBook(self, book, count):
        cost = book.price * count
        if cost > self.total_money:
            max_count = self.total_money // book.price
            if max_count == 0:
                return 0
            self.books[book] = self.books.get(book, 0) + max_count
            self.total_money -= book.price * max_count
            return max_count
        else:
            self.books[book] = self.books.get(book, 0) + count
            self.total_money -= cost
            return count

    # do'konda kitoblar borligini tekshirish
    def hasBook(self):
        return any(qty > 0 for qty in self.books.values())

    # ma'lum turdagi kitob borligini tekshirish
    def hasBookType(self, book):
        return self.books.get(book, 0) > 0

    # ma'lum kitobdan sotish
    def sell(self, book, count):
        available = self.books.get(book, 0)
        if available == 0:
            return 0
        sell_count = min(count, available)
        self.books[book] -= sell_count
        return sell_count

    # do'kondagi pulni olish
    def getMoney(self):
        return self.total_money

    # ma'lum kitobdan mavjud soni
    def getCount(self, book=None):
        if book:
            return self.books.get(book, 0)
        else:
            return sum(self.books.values())

    # do'kon nomi
    def getBookShopName(self):
        return self.name


# ==== Test kodi ====
def checkTest(result, expected):
    if result != expected and (expected is not None and expected != result):
        raise ArithmeticError(f"Natija xato: {result} != {expected}")


# test misol
book1 = Book("C++", 20_000)
book2 = Book("Java", 25_000)
book3 = Book("Kotlin", 25_000)

shop = BookShop("Kitoblar olami", 1_000_000)

checkTest(shop.hasBook(), False)
checkTest(shop.hasBookType(book1), False)
checkTest(shop.sell(book1, 1), 0)
checkTest(shop.buyBook(book1, 40), 40)
checkTest(shop.getMoney(), 200_000)
checkTest(shop.buyBook(book2, 20), 8)
checkTest(shop.hasBook(), True)
checkTest(shop.hasBookType(book1), True)
checkTest(shop.sell(book1, 1), 1)
checkTest(shop.sell(book3, 1), 0)
checkTest(shop.getMoney(), 0)
checkTest(shop.getCount(book1), 39)
checkTest(shop.getCount(), 47)
checkTest(shop.getBookShopName(), "Kitoblar olami")

print("✅ Barcha testlar muvaffaqiyatli o‘tdi!")
