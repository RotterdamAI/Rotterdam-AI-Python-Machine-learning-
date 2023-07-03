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

# Area rectancle

def hint_area_rectangle():
    print("We can store and calculate the area of a rectangle by using:\n`result = length * width`.")

def test_area_rectangle(f):
    loader()
    assert(f(3, 4) == 12)
    correct_assertion()

# Convert Fahrenheit to celsius

def hint_fahr_to_cel():
    print("celsius = (fahrenheit - 32) * 5/9 and also make sure you return the value so the test can see if its correct")

def test_fahr_to_cel(f):
    loader()
    assert(f(41) == 5.0)
    assert(f(-4) == -20.0)
    correct_assertion()

# Count A names

def hint_count_A_names():
    print("We can use a for loop to loop over all the names like: for name in names:")
    print("We can then check if the first letter of the name starts with an A by getting the index of the first letter: name[0]")

def test_count_A_names(f):
    loader()
    assert(f(["Alice", "Bob", "Amy", "Alex"]) == 3)
    assert(f(["Alice", "Bob"]) == 1)
    assert(f(["Bob"]) == 0)
    correct_assertion()

# getting the average

def hint_get_average():
    print("we can loop over all the number and add it up to a total, after getting the total we can do a division like total/len(numbers) to get the average")

def test_get_average(f):
    loader()
    assert(f([1,2,3,4,5]) == 3.0)
    assert(f([1,2,7,5]) == 3.75)
    correct_assertion()

