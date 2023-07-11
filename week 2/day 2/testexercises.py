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

