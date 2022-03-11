# coding = utf-8(

X = 1

def nester():
    X = 2
    print(X)                        # Global: 1
    class C:
        print(X)                    # Global: 1
        def method1(self):
            print(X)                # Global: 1
        def method2(self):
            X = 3                   # Hides global
            print(X)                # Local: 3

    I = C()
    I.method1()
    I.method2()

def nester2():
    X = 2                           # Hides global
    print(X)                        # Local: 2
    class C:
        print(X)                    # In enclosing def(nester): 2
        def method1(self):
            print(X)                # In enclosing def(nester): 2
        def method2(self):
            X = 3                   # Hides enclosing (nester)
            print(X)                # Local: 3

    I = C()
    I.method1()
    I.method2()


def nester3():
    X = 2                           # Hides global
    print(X)                        # Local: 2
    class C:
        X = 3                       # Class local hides nester's: C.X or I.X(not scoped)
        print(X)                    # Local: 3
        def method1(self):
            print(X)                # In enclosing def(not 3 in class!): 2
            print(self.X)           # Inherited class local: 3
        def method2(self):
            X = 4                   # Hides enclosing (nester, not class)
            print(X)                # Local: 4
            self.X = 5              # Hides class
            print(self.X)           # Located in instance: 5

    I = C()
    I.method1()
    I.method2()


class Super:
    def hello(self):
        self.data1 = 'spam'

class Sub(Super):
    def hola(self):
        self.data2 = 'eggs'


if __name__ == '__main__':
    print(X)                        # Global: 1
    nester()                        # Rest: 1,1,1,3
    print('-'*40)
    print(X)
    nester2()
    print('-' * 40)
    print(X)
    nester3()
    print('-' * 40)
    X = Sub()
    print(X.__dict__)               # Instance namespace dict
    print(X.__class__)              # Class of instance
    print(Sub.__bases__)            # Superclasses of class
    print(Super.__bases__)          # () empty tuple in Python 2.X
    print('-' * 40)
    Y = Sub()
    X.hello()
    print(X.__dict__)
    X.hola()
    print(X.__dict__)
    print(list(Sub.__dict__.keys()))
    print(list(Super.__dict__.keys()))
    print(Y.__dict__)
    print('-' * 40)
    print(X.data1, X.__dict__['data1'])
    X.data3 = 'toast'
    print(X.__dict__)
    X.__dict__['data3'] = 'ham'
    print(X.data3)