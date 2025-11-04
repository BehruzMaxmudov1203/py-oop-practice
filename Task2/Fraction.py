# 4️⃣ Kasr sinfi
class Fraction:
    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator

    def add(self, other: 'Fraction'):
        """Ikki kasrni qo'shish"""
        if self.denominator == other.denominator:
            self.numerator += other.numerator
        else:
            self.numerator = self.numerator * other.denominator + other.numerator * self.denominator
            self.denominator *= other.denominator



if __name__ == "__main__":
    
    frac1 = Fraction(1, 2)
    frac2 = Fraction(1, 3)
    frac1.add(frac2)
    print(f"Yangi kasr: {frac1.numerator}/{frac1.denominator}")


