class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def equals(self, other: 'Rectangle') -> bool:
        """Ikki rectangle tengligini tekshirish"""
        return self.width == other.width and self.height == other.height
    



if __name__ == "__main__":
    
    r1 = Rectangle(5, 10)
    r2 = Rectangle(5, 10)
    print(f"Tengmi: {r1.equals(r2)}")

