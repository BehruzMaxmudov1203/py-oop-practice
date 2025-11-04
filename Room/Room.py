class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Room (Xona) sinfi
class Room:
    def __init__(self, capacity):
        self.capacity = capacity     # Xonaga nechta talaba sig‘adi
        self.students = []           # Xonadagi talabalar ro‘yxati

    # Talaba qo‘shish metodi
    def add(self, student):
        if len(self.students) < self.capacity:
            self.students.append(student)
            return True   # Muvaffaqiyatli qo‘shildi
        else:
            return False  # Joy yo‘q

    # Xona to‘lganligini tekshiradi
    def isFull(self):
        return len(self.students) >= self.capacity

    # Xona bo‘shligini tekshiradi
    def isEmpty(self):
        return len(self.students) == 0

    # Xonadagi talabalarni ko‘rsatadi
    def show(self):
        if self.isEmpty():
            print("Xonada hech qanday talaba yo‘q.")
        else:
            print("Xonadagi talabalar:")
            for s in self.students:
                print(f"- {s.name}, {s.age} yosh")


# ==== Dasturni tekshirish ====
s1 = Student("Alisa", 18)
s2 = Student("Bekzod", 19)
s3 = Student("Dilshod", 20)
s4 = Student("Malika", 21)
s5 = Student("Sardor", 22)

r = Room(4)

print(r.add(s1))  # True
print(r.add(s2))  # True
print(r.add(s3))  # True
print(r.add(s4))  # True
print(r.add(s5))  # False (sig‘imdan oshdi)
print(r.isFull())  # True
print(r.isEmpty()) # False
r.show()
