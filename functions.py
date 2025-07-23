def greet():
    print("Hello, welcome to Python functions!")
greet()

def greet_user(name):
    print("Hello", name)
greet_user("Alice")

def add_numbers(a, b):
    print("The sum is:", a + b)
add_numbers(5, 3)

def multiply(a, b):
    result = a * b
    return result
product = multiply(4, 5)
print("Product is:", product)

def greet(name="Guest"):
    print("Hello", name)
greet("Sam")
greet()

def square(x):
    return x * x
def display_square(num):
    result = square(num)
    print("Square is:", result)
display_square(6)

def calculate(a, b):
    sum_ = a + b
    diff = a - b
    return sum_, diff
s, d = calculate(10, 3)
print("Sum:", s)
print("Difference:", d)

def say_hello():
    print("Hello!")
def greet_person(name):
    say_hello()
    print("Nice to meet you,", name)
greet_person("Emma")