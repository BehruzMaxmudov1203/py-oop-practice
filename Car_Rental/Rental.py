class Car:
    def __init__(self, model: str, number: str):
        self.model = model
        self.number = number

    def __eq__(self, other):
        if not isinstance(other, Car):
            return False
        return self.model == other.model and self.number == other.number

    def __hash__(self):
        return hash((self.model, self.number))

    def __repr__(self):
        return f"Car({self.model}, {self.number})"


class CarRental:
    def __init__(self, name: str):
        self.name = name
        self.cars = set()  # tizimga qo'shilgan avtomobillar
        self.rented_cars = {}  # {Car: customer_name}

    def add_car(self, car: Car) -> bool:
        """Avtomobilni tizimga qo'shadi"""
        if car in self.cars:
            return False
        self.cars.add(car)
        return True

    def rent_car(self, car: Car, customer: str) -> bool:
        """Avtomobilni ijaraga beradi"""
        if car not in self.cars or car in self.rented_cars:
            return False
        self.rented_cars[car] = customer
        return True

    def return_car(self, car: Car) -> bool:
        """Ijaradan qaytaradi"""
        if car not in self.rented_cars:
            return False
        del self.rented_cars[car]
        return True

    def has_car(self, car: Car) -> bool:
        """Tizimda mavjudligini tekshiradi"""
        return car in self.cars

    def is_rented(self, car: Car) -> bool:
        """Ijarada ekanligini tekshiradi"""
        return car in self.rented_cars

    def get_available_cars(self) -> set:
        """Hozirda ijaraga berilmagan avtomobillar ro'yxati"""
        return self.cars - set(self.rented_cars.keys())

    def get_renter(self, car: Car):
        """Avtomobilni kim ijaraga olganini qaytaradi"""
        return self.rented_cars.get(car, None)



def main():
    car1 = Car("Chevrolet Malibu", "AA1234BB")
    car2 = Car("Hyundai Sonata", "CC5678DD")
    car3 = Car("Toyota Corolla", "EE9101FF")

    rental = CarRental("Avto Rent")

    assert rental.add_car(car1) is True
    assert rental.add_car(car2) is True
    assert rental.add_car(car1) is False  # Car already exists

    assert rental.rent_car(car3, "Sherzod") is False  # Car not available
    assert rental.rent_car(car1, "Sherzod") is True   # Renting successful
    assert rental.rent_car(car1, "Aziz") is False     # Already rented

    assert rental.is_rented(car1) is True
    assert rental.is_rented(car2) is False

    assert rental.get_renter(car1) == "Sherzod"

    assert rental.return_car(car1) is True
    assert rental.return_car(car1) is False  # Already returned
    assert rental.is_rented(car1) is False

    assert len(rental.get_available_cars()) == 2  # car1 returned, 2 cars available
    print("All tests passed ✅")

main()
