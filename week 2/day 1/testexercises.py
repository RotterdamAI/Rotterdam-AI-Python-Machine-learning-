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


def hint_zip_name_age():
    print("don't forget to wrap your zip() function around a list(zip(names, ages)) to make sure it is of type list")

def test_zip_name_age(f):
    loader()
    assert(f(["Alice", "Bob", "Charlie", "David"],[25, 32, 18, 47]))
    correct_assertion()

def hint_filter_even_numbers():
    print("Don't forget to use the is_even function within the filter function.")
    print("Use the list around filter like list(filter(x, y)) to return a list object")

def test_filter_even_numbers(f):
    loader()
    assert(f([1,2,3,4,5,6]) == [2, 4, 6])
    correct_assertion()

def hint_map_celsius_to_fahrenheit():
    print("Dont forget to wrap output of map around a list() like list(map(celsius_to_fahrenheit, celsius_list))")

def test_map_celsius_to_fahrenheit(f):
    loader()
    assert(f([0, 10, 25, 32, 100]) == [32.0, 50.0, 77.0, 89.6, 212.0])
    correct_assertion()

def hint_count_words():
    print("Read in the file exercise4.txt then when we have the content we can use .split() function to get all words in a list and then we can count the lenght of that list")

def test_count_words(f):
    loader()
    assert(f() == 69)
