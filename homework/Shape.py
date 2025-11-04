class Shape:
    def __init__(self, name, color, perimeter, square):
        self.name = name
        self.color = color
        self.perimeter = perimeter
        self.square = square

    def show(self):
        print(f"Shakl nomi: {self.name}")
        print(f"Rangi: {self.color}")
        print(f"Perimetri: {self.perimeter}")
        print(f"Yuzi: {self.square}")

    def showPerimeter(self):
        print(f"{self.name} perimetri: {self.perimeter}")



shape1 = Shape("Kvadrat", "Qizil", 40, 100)
shape1.show()
shape1.showPerimeter()