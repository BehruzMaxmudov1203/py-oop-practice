class Student:
    def __init__(self, last_name: str, first_name: str, course: str):
        self.last_name = last_name
        self.first_name = first_name
        self.course = course  # studentning kursi yoki guruhga mos keladigan identifikator

    def __str__(self):
        """Student haqida ma'lumot"""
        return f"{self.last_name} {self.first_name} ({self.course})"


class Group:
    MAX_STUDENTS = 20  # har bir guruhdagi maksimal talaba soni

    def __init__(self, name: str, course: str):
        self.name = name
        self.course = course  # guruh kursi
        self.students = []  # guruhdagi talabalar ro'yxati

    def add(self, student: Student) -> bool:
        """Guruhga student qo'shish"""
        if len(self.students) >= self.MAX_STUDENTS:
            return False  # guruh to'la
        if student.course != self.course:
            return False  # kurs mos kelmaydi
        self.students.append(student)
        return True

    def is_empty(self) -> bool:
        """Guruh bo'shligini tekshirish"""
        return len(self.students) == 0

    def is_full(self) -> bool:
        """Guruh to'la ekanligini tekshirish"""
        return len(self.students) >= self.MAX_STUDENTS

    def __str__(self):
        """Guruh va tarkibidagi talabalarni chiqarish"""
        if self.is_empty():
            return f"Guruh: {self.name} (bo'sh)"
        students_list = "\n".join(str(s) for s in self.students)
        return f"Guruh: {self.name}\nTalabalar:\n{students_list}"


# ===== Misol ishlatish =====
if __name__ == "__main__":
    student1 = Student("Olimova", "Aziza", "Android GITA1")
    student2 = Student("Karimov", "Jasur", "Android GITA1")
    student3 = Student("Tursunov", "Azamat", "iOS GITA1")  # kurs mos emas

    group = Group("Android GITA1", "Android GITA1")

    print(group.add(student1))  # True
    print(group.add(student2))  # True
    print(group.add(student3))  # False, kurs mos emas

    print(group.is_full())   # False
    print(group.is_empty())  # False

    print(group)  # guruh tarkibi chiqariladi
