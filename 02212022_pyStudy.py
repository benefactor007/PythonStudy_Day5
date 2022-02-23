# coding=utf-8

# Page 778

class C2:
    pass

class C3:
    pass

class C1(C2,C3):
    # def setname(self,who):
    #     self.name = who
    def __init__(self,who):
        self.name = who

# class FirstClass:
#     def setdata(self,value):
#         self.data = value
#     def display(self):
#         print(self.data)

# def main():
#     I1 = C1('bob')
#     I2 = C1('sue1')
#     # print(I1.name)
#     # I1.setname('bob')
#     # I2.setname('sue1')
#     print(I1.name)

# from modulename import  FirstClass
import modulename
class SecondClass(modulename.FirstClass):
    def display(self):
        print('Current value = "%s"' % self.data)

def main():
    x = modulename.FirstClass()
    y = modulename.FirstClass()
    x.setdata("King Arthur")
    y.setdata("3.14159")
    x.display()                  # Prints "King Arthur"
    y.display()
    x.data = "New value"
    x.display()
    x.anothername = "spam"      # Can set new attributes here too!
    print(x.anothername)
    z = SecondClass()
    z.setdata(42)
    z.display()
    print(z.data)


if __name__ == '__main__':
    main()