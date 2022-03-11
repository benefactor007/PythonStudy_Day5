# coding=utf-8

class MixedNames:                                       # Define class
    data = 'spam'                                       # Assign class attr
    def __init__(self,value):                           # Assign method name
        self.data = value                               # Assign instance attr
    def display(self):
        print(self.data, MixedNames.data)               # Instances attr, class attr


class NextClass:                                        # Define class
    def printer(self, text):                            # Define method
        self.message = text                             # Change instance
        print(self.message)                             # Access instance

class Super:
    def __init__(self, x):
        # ... default code ...
        pass
    def method(self):
        print('in Super.method')


class Sub(Super):
    def __init__(self, x, y):
        super.__init__(self, x)                         # Run superclass __init
        # ... custom code ...                           # Do myy init actions
    def method(self):                                   # Override method
        print('Starting Sub.method')                    # Add actions here
        Super.method(self)                              # Run default action
        print('Ending Sub.method')



if __name__ == '__main__':
    # x = MixedNames(1)                                   # Make two instance objects
    # y = MixedNames(2)                                   # Each has its own data
    # x.display(); y.display()                            # self.data differs, MixedNames.data is the same.

    # x = NextClass()                                     # Make instance
    # x.printer('instance call')                          # Call its method
    # print(x.message)                                    # Instance changed
    # NextClass.printer(x, 'class call')                  # Direct class call
    # print(x.message)                                    # Instance changed again
    # # NextClass.printer('bad call')                     # TypeError:
    #                                                     # printer() missing 1 required positional argument: 'text'

    # I = Sub(1,2)
    x = Super()                                         # Make a Super instance
    x.method()                                          # Runs Super.method

    x = Sub()                                           # Make a Sub instance
    x.method()                                          # Runs Sub.method, calls Super.method



