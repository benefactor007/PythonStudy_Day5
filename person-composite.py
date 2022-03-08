# coding=utf-8

class Person(object):
    def __init__(self, name, job=None, pay=0):  # Normal function args
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):  # Behavior methods
        return self.name.split()[-1]  # self is implied subject

    # @rangetest(percent=(0,0 ,1.0))              # Use decorator to validate
    def giveRaise(self, percent):
        # self.pay = int(self.pay * (1 + percent))        # Must change here only
        self.pay = self.pay * (1 + percent)

    # Add __repr__ overload method for printing object
    def __repr__(self):  # Added method
        return '[Person: %s, %.2f]' % (self.name, self.pay)  # String to print


class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)  # Embed a Person object

    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus)  # Intercept and delegate

    def __getattr__(self, attr):
        return getattr(self.person, attr)  # Delegate all other attrs

    def __repr__(self):
        return str(self.person)  # Must overload again (in 3.X)


if __name__ == '__main__':
    jon = Person('Jiahao Wu')  # Test the class
    dynasty = Person('Tianyuan Xu', job='Warrior', pay=50000)  # Runs __init__ automatically
    print(jon.name, jon.pay)  # Fetch attached attributes
    print(dynasty.name, dynasty.pay)  # Jon's and Dynasty's attrs differ
    print('{0} {1}'.format(dynasty.name, dynasty.pay))
    print('%s %s' % (dynasty.name, dynasty.pay))
    # print(jon.name.split()[-1])
    # dynasty.pay *= 1.10
    # print('%.2f' % dynasty.pay)
    print(jon.lastName(), dynasty.lastName())
    dynasty.giveRaise(.10)
    print(dynasty.pay)
    print('%.2f' % dynasty.pay)
    print('{0:.2f}'.format(dynasty.pay))
    print(round(dynasty.pay, 2))
    print(dynasty)
    print(jon)
    # name = 'Jiahao Wu'
    # print(name.split())
    # print(name.split()[-1])
    # # Simple variable, outside class
    # pay = 100000000                  # Give a 10% raise
    # pay *= 1.10                      # or: pay = pay * 1.10, if you like to type
    # print('%.2f' % pay)              # or: pay = pay + (pay * .10), if you _really_ do!
    # xiuge = Manager('Xuping Lu', 'mgr', 50000)
    xiuge = Manager('Xuping Lu', 50000)  # Job name not needed
    xiuge.giveRaise(.10)  # instance.method(args..); Implied/set by class
    # Manager.giveRaise(xiuge, .10)      # class.method(instance,args...)
    print(xiuge.lastName())
    print(xiuge)
    print('--All three--')
    for obj in (jon, dynasty, xiuge):  # Process objects generically {jəˈnerəklē}
        obj.giveRaise(.10)  # Run this object's giveRaise
        print(obj)  # Run the common __repr__
    """Or to paraphrase a movie line: Python's super is like a box of chocolates -you never know what you're going
        to get!"""
