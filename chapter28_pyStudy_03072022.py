# coding=utf-8
# File Person.py (start)
# class Person:              # Start a class
#     def __int__(self, name, job, pay):          # Constructor takes three arguments
#         self.name = name                        # Fill out fields when created
#         self.job = job                          # self is the new instance object
#         self.pay = pay

# Add defaults for constructor arguments

# from __future__ import print_function           # Input Python3.X print method to fix parentheses issue

class Person(object):
    def __init__(self, name, job=None, pay=0):  # Normal function args
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):                         # Behavior methods
        return self.name.split()[-1]            # self is implied subject
    # @rangetest(percent=(0,0 ,1.0))              # Use decorator to validate
    def giveRaise(self, percent):
        # self.pay = int(self.pay * (1 + percent))        # Must change here only
        self.pay = self.pay * (1 + percent)
    # Add __repr__ overload method for printing object
    def __repr__(self):                                         # Added method
        return '[Person: %s, %.2f]' % (self.name, self.pay)     # String to print

# {augment: make (something) greater by adding to it; increase.}
# Add customization of one behavior in a subclass
class Manager(Person):                  # Define a subclass of Person; Inherit Person attrs
    def giveRaise(self, percent, bonus = .10):                  # Redefine to customize; redefine at this level
        # self.pay = int(self.pay * (1 + percent + bonus))          # Bad: cut and pastel
        Person.giveRaise(self, percent + bonus)                     # Good: augment original; instance.method(args..)
        # Call Person's version
        # Python will convert to class.method(instance,args...)


# Add incremental self-test code

# {Fetch: go for and then bring back}

# def main():
# Allow this file to be imported as well as run/tested
if __name__ == '__main__':  # When run for testing only
    jon = Person('Jiahao Wu')  # Test the class
    dynasty = Person('Tianyuan Xu', job='Warrior', pay=50000)  # Runs __init__ automatically
    print(jon.name, jon.pay)  # Fetch attached attributes
    print(dynasty.name, dynasty.pay)  # Jon's and Dynasty's attrs differ
    print('{0} {1}'.format(dynasty.name,dynasty.pay))
    print('%s %s'%(dynasty.name,dynasty.pay))
    # print(jon.name.split()[-1])
    # dynasty.pay *= 1.10
    # print('%.2f' % dynasty.pay)
    print(jon.lastName(), dynasty.lastName())
    dynasty.giveRaise(.10)
    print(dynasty.pay)
    print('%.2f' % dynasty.pay)
    print('{0:.2f}'.format(dynasty.pay))
    print(round(dynasty.pay,2))
    print(dynasty)
    print(jon)
    # name = 'Jiahao Wu'
    # print(name.split())
    # print(name.split()[-1])
    # # Simple variable, outside class
    # pay = 100000000                  # Give a 10% raise
    # pay *= 1.10                      # or: pay = pay * 1.10, if you like to type
    # print('%.2f' % pay)              # or: pay = pay + (pay * .10), if you _really_ do!
    xiuge = Manager('Xuping Lu', 'mgr', 50000)
    xiuge.giveRaise(.10)               # instance.method(args..)
    # Manager.giveRaise(xiuge, .10)      # class.method(instance,args...)
    print(xiuge.lastName())
    print(xiuge)
    print('--All three--')
    for obj in (jon,dynasty,xiuge):             # Process objects generically {jəˈnerəklē}
        obj.giveRaise(.10)                      # Run this object's giveRaise
        print(obj)                              # Run the common __repr__
    """Or to paraphrase a movie line: Python's super is like a box of chocolates -you never know what you're going
        to get!"""

