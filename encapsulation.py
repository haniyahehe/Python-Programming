class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age > 0:
            self.__age = new_age
        else:
            print("Age must be a positive number!")

person1 = Person("Haniyah", 15)

print("Name:", person1.name)

print("Age:", person1.get_age())

person1.set_age(17)
print("Updated Age:", person1.get_age())

person1.set_age(-5)