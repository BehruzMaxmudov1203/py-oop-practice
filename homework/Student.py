class Student:
    def __init__(self, name, course, age):
        self.name = name
        self.course = course
        self.age = age

    def info(self):
        print(f"Talaba ismi: {self.name}")
        print(f"Kursi: {self.course}")
        print(f"Yoshi: {self.age}")



student1 = Student("Behruz", 2, 20)
student1.info()

