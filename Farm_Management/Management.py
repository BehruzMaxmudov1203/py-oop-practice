class Crop:
    def __init__(self, name: str, growth_days: int, yield_per_hectare: int):
        self.name = name
        self.growth_days = growth_days
        self.yield_per_hectare = yield_per_hectare

    def __eq__(self, other):
        if not isinstance(other, Crop):
            return False
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return f"Crop({self.name}, {self.growth_days}d, {self.yield_per_hectare}kg/ha)"


class Field:
    def __init__(self, name: str, total_area: int):
        self.name = name
        self.total_area = total_area
        self.crops = {}  # {Crop: area_planted}

    def plant_crop(self, crop: Crop, area: int) -> bool:
        """Dalaga ekin ekadi"""
        available_area = self.get_available_area()
        if area > available_area:
            return False
        if crop in self.crops:
            self.crops[crop] += area
        else:
            self.crops[crop] = area
        return True

    def harvest_crop(self, crop: Crop) -> int:
        """Ekinni yig‘ib oladi va hosilni hisoblaydi"""
        if crop not in self.crops:
            return 0
        area = self.crops[crop]
        yield_amount = area * crop.yield_per_hectare
        del self.crops[crop]  # ekin dala bo‘shadi
        return yield_amount

    def get_available_area(self) -> int:
        """Bo‘sh maydonni qaytaradi"""
        used_area = sum(self.crops.values())
        return self.total_area - used_area

    def __repr__(self):
        return f"Field({self.name}, total_area={self.total_area}, crops={self.crops})"


# 3️⃣ Farm class
class Farm:
    def __init__(self, name: str):
        self.name = name
        self.fields = set()  # Set of Field objects

    def add_field(self, field: Field) -> bool:
        """Fermer xo‘jaligiga dala qo‘shadi"""
        if field in self.fields:
            return False
        self.fields.add(field)
        return True

    def get_field_by_name(self, name: str):
        """Nom bo‘yicha dala topadi"""
        for field in self.fields:
            if field.name == name:
                return field
        return None

    def calculate_total_yield(self) -> int:
        """Barcha dalalardagi ekinlardan olinadigan umumiy hosil"""
        total_yield = 0
        for field in self.fields:
            for crop, area in field.crops.items():
                total_yield += area * crop.yield_per_hectare
        return total_yield



def main():
    wheat = Crop("Wheat", 120, 2000)
    rice = Crop("Rice", 90, 3000)
    corn = Crop("Corn", 100, 2500)

    field1 = Field("Field-1", 10)
    field2 = Field("Field-2", 15)

    farm = Farm("My Farm")

    assert farm.add_field(field1) is True
    assert farm.add_field(field2) is True
    assert farm.add_field(field1) is False  # already exists

    assert field1.plant_crop(wheat, 5) is True
    assert field1.plant_crop(rice, 3) is True
    assert field1.plant_crop(corn, 5) is False  # not enough space

    assert field1.get_available_area() == 2

    assert field1.harvest_crop(rice) == 3 * 3000  # 9000
    assert field1.get_available_area() == 7

    assert farm.calculate_total_yield() == 0  # harvested rice removed

    field1.plant_crop(corn, 3)
    field2.plant_crop(wheat, 10)
    assert farm.calculate_total_yield() == 3*2500 + 10*2000  # 20000

    print("All tests passed ✅")

main()
