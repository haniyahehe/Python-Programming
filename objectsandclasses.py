class Car:
    def __init__(self, brand, model, year):
        self.brand = brand  # Attribute 1
        self.model = model  # Attribute 2
        self.year = year    # Attribute 3

    def start(self):
        print(f"The {self.brand} {self.model} is starting... Vroom!")

    def display_info(self):
        print("Car Information:")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print("-" * 30)

car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()
car1.start()

car2 = Car("Tesla", "Model S", 2022)
car2.display_info()
car2.start()

car3 = Car("Ford", "Mustang", 1967)
car3.display_info()
car3.start()