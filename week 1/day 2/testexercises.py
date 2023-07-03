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

def hint_first_last_letter():
    print("Remember we can acces the last letter by using text[-1]")
    print("also note we can add 2 string together by using a +")

def test_first_last_letter(f):
    loader()
    assert(f("test") == "tt")
    assert(f("next") == "nt")
    correct_assertion()

def hint_reverse_string():
    print("Have you thought about looping over the text? If your lazy you might figure out what [::-1] does.")

def test_reverse_string(f):
    loader()
    assert(f("test") == "tset")
    assert(f("correct") == "tcerroc")
    correct_assertion()

def hint_is_palindrome():
    print("We can use the same logic as the previous exercise and check if its equal to the input.")

def test_is_palindrome(f):
    loader()
    assert(f("test") == False)
    assert(f("racecar") == True)
    correct_assertion()

def hint_in_list():
    print("you can check if the string is in the list_obj by using the `in` operator")

def test_in_list(f):
    loader()
    assert(f(["test", "hello"], "hello") == True)
    assert(f(["test", "hello"], "notin") == False)
    correct_assertion()

def hint_custom_sort_list():
    print("You can zip the 2 list together using the zip function.")
    
def test_custom_sort_list(f):
    loader()
    assert(f(["3", "test", "2", "1"], [3, 0, 2, 1]) == ["test", "1", "2", "3"])
    correct_assertion()