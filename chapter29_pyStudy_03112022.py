# coding=utf-8


# delegate: verb. entrust (a task or responsibility) to another person, typically one who is less senior than oneself.
# the power delegated to him must never be misused
from abc import ABCMeta, abstractmethod


class Super(metaclass=ABCMeta):

    def method(self):
        pass

    def delegate(self):
        self.action()
    @abstractmethod
    def action(self):
        pass


class Sub(Super):
    def action(self):
        print('spam')


if __name__ == '__main__':
    # X = Super()               # TypeError: Can't instantiate abstract class Super with abstract methods method
    # X = Sub()                 # TypeError: Can't instantiate abstract class Sub with abstract methods method
    X = Sub()
    X.delegate()
