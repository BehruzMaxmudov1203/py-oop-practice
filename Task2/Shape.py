class Shape:
    def __init__(self, name: str, color: str, area: float, perimeter: float, sides: int):
        self.name = name
        self.color = color
        self.area = area
        self.perimeter = perimeter
        self.sides = sides

    def get_size(self) -> int:
        """Shakl tomonlari sonini qaytaradi"""
        return self.sides

if __name__ == "__main__":
  
    s = Shape("Uchburchak", "Yashil", 12.5, 15.0, 3)
    print(f"Tomonlar soni: {s.get_size()}")
