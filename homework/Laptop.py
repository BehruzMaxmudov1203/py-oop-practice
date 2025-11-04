class Laptop:
    def __init__(self, screenSize, batteryCellCount, modelName, serialNumber, color):
        self.screenSize = screenSize
        self.batteryCellCount = batteryCellCount
        self.modelName = modelName
        self.serialNumber = serialNumber
        self.color = color

    def show(self):
        print(f"Model nomi: {self.modelName}")
        print(f"Ekran o‘lchami: {self.screenSize} dyuym")
        print(f"Batareya hujayralari soni: {self.batteryCellCount}")
        print(f"Seriya raqami: {self.serialNumber}")
        print(f"Rangi: {self.color}")

laptop1 = Laptop("15.6", 4, "ASUS Vivobook", "SN123456", "Kulrang")
laptop1.show()
