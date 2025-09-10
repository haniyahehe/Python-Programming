class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

    def move(self):
        print(f"{self.name} is moving.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

    def fetch(self):
        print(f"{self.name} is fetching the ball!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

    def climb(self):
        print(f"{self.name} is climbing the tree!")

animal1 = Animal("Generic Animal")
animal1.speak()
animal1.move()
print("----------------------")

dog1 = Dog("Puppy")
dog1.speak()
dog1.move()
dog1.fetch()
print("----------------------")

cat1 = Cat("Kitten")
cat1.speak()
cat1.move()
cat1.climb()