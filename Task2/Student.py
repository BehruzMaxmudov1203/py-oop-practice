class Student:
    def __init__(self, student_id: int, name: str, age: int, course: str):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course

    def show(self):
        """Talaba ma'lumotlarini chiqarish"""
        print(f"ID: {self.student_id}, Ism: {self.name}, Yosh: {self.age}, Kurs: {self.course}")


if __name__ == "__main__":
    
    st = Student(1, "Alisa", 18, "3-kurs")
    st.show()

