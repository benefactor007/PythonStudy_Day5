# coding=utf-8

# File person-department.py
# Aggregate embedded object into a composite

from chapter28_pyStudy_03072022 import Person, Manager

class Department:
    def __init__(self, *args):
        self.members = list(args)
    def addMember(self, person):
        self.members.append(person)
    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)
    def showAll(self):
        for person in self.members:
            print(person)

if __name__ == '__main__':
    jon = Person('Jiahao Wu')  # Test the class
    dynasty = Person('Tianyuan Xu', job='Warrior', pay=50000)  # Runs __init__ automatically
    xiuge = Manager('Xuping Lu', 50000)  # Job name not needed

    development = Department(jon,dynasty)
    development.addMember(xiuge)
    development.giveRaises(.10)
    development.showAll()