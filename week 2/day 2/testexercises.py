from time import sleep
import sys
OKGREEN = '\033[92m'
ENDC = '\033[0m'

#################################################
# helper functions
#################################################
def correct_assertion():
    print(f"\n{OKGREEN}All tests passed!!!"+ ENDC)

def loader():
    for i in range(10):
        sys.stdout.write("\r{0}>".format("="*i))
        sys.stdout.flush()
        sleep(0.1)

#################################################
# exercise tests
#################################################

def hint_BankAccount():
    print("dont forget to use initialization for the 2 arguments like self.account_number = account_number")
    print("We can access our init from deposit using for example self.amount += amount")

def test_BankAccount(f):
    loader()
    x = f("test", 500)
    assert(x.get_balance() == 500)
    x.deposit(500)
    assert(x.get_balance() == 1000)
    x.withdraw(500)
    assert(x.get_balance() == 500)
    correct_assertion()

def hint_Book():
    print("dont forget to initialize using self.title = title etc...")
    print("make sure to return the right display info if you have problems use this: return f'Title: {self.title}, Author: {self.author}, Year: {self.year}'")

def test_Book(f):
    loader()
    x = f("testbook", "testauthor", 9999)
    assert(x.get_title() == "testbook")
    assert(x.get_author() == "testauthor")
    assert(x.get_year() == "9999")


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("An animal makes a sound.")

# Define the Dog class
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        print("The dog barks.")

# Define the Cat class
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("The cat meows.")

# Create instances of the classes
animal = Animal("Generic Animal", 5)
dog = Dog("Buddy", 3, "Labrador")
cat = Cat("Whiskers", 2, "Gray")

# Call the speak() method on each object
animal.speak()
dog.speak()
cat.speak()


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __add__(self, object):
        if isinstance(object, Vector):
            new_x = self.x + object.x
            new_y = self.y + object.y
            return Vector(new_x, new_y)
        else:
            raise TypeError("Unsupported operand type for +: 'Vector' and {}".format(type(object).__name__))
    
    
    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            new_x = self.x * scalar
            new_y = self.y * scalar
            return Vector(new_x, new_y)
        else:
            raise TypeError("Unsupported operand type for *: 'Vector' and '[]'".format(type(scalar).__name__))