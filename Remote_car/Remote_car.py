class Battery:
    VOLTAGE = 1.5  # constant voltage in volts

    def __init__(self, capacity_mAh: int):
        self.capacity_mAh = capacity_mAh  # total capacity
        self.charge_mAh = capacity_mAh    # current charge

    def get_power(self) -> float:
        """
        Calculates power: P = I * U
        I = current in mA, U = voltage in volts
        Returns power in mW (milliwatt)
        """
        return self.charge_mAh * self.VOLTAGE

    def use(self, amount_mAh: int) -> bool:
        """
        Uses specified mAh from the battery.
        Returns True if battery had enough charge, False otherwise.
        """
        if self.charge_mAh >= amount_mAh:
            self.charge_mAh -= amount_mAh
            return True
        return False

    def get_charge_percent(self) -> int:
        return int((self.charge_mAh / self.capacity_mAh) * 100)


class RemoteCar:
    def __init__(self, battery_slots: int, motor_power: float):
        self.battery_slots = battery_slots
        self.motor_power = motor_power  # motor power in mW
        self.batteries: list[Battery] = []

    def add_battery(self, battery: Battery) -> bool:
        """
        Adds a battery to the car.
        Returns True if added successfully, False if slots full.
        """
        if len(self.batteries) < self.battery_slots:
            self.batteries.append(battery)
            return True
        return False

    def get_battery_info(self) -> list[int]:
        """
        Returns a list of battery charge percentages
        """
        return [b.get_charge_percent() for b in self.batteries]

    def run(self, minutes: int) -> bool:
        """
        Tries to run the car for given minutes.
        Requires total battery power >= motor power.
        Consumes battery proportionally.
        """
        if len(self.batteries) < self.battery_slots:
            return False  # not enough batteries

        total_power = sum(b.get_power() for b in self.batteries)
        required_power = self.motor_power * minutes

        if total_power < required_power:
            return False  # not enough power

        # Consume power proportionally from all batteries
        remaining_required = required_power
        for b in self.batteries:
            if remaining_required <= 0:
                break
            available = b.get_power()
            used = min(available, remaining_required)
            b.use(used / Battery.VOLTAGE)  # convert power back to mAh
            remaining_required -= used

        return True


# ===== Example usage =====
if __name__ == "__main__":
    car = RemoteCar(battery_slots=2, motor_power=50)  # motor power 50 mW per minute
    b1 = Battery(100)  # 100 mAh
    b2 = Battery(120)  # 120 mAh

    print(car.add_battery(b1))  # True
    print(car.add_battery(b2))  # True
    print(car.add_battery(Battery(80)))  # False, slots full

    print("Battery info:", car.get_battery_info())  # [100, 100]

    can_run = car.run(1)  # run 1 minute
    print("Car can run:", can_run)
    print("Battery info after run:", car.get_battery_info())
