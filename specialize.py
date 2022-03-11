# coding=utf-8

# verbatim, vərˈbādəm, in exactly the same words as were used originally.
# subjects were instructed to recall the passage verbatim

class Super:
    def method(self):
        print("in Super.method")  # Default behavior

    def delegate(self):
        self.action()  # Expected to be defined
    def action(self):
        # assert False, 'action must be defined!'                      # If this version is called
        raise NotImplementedError('action must be defined')

class Inheritor(Super):  # Inherit method verbatim
    pass


class Replacer(Super):  # Replace method completely
    def method(self):
        print('in Replacer.method')


class Extender(Super):  # Extend method behavior
    def method(self):
        print('starting Extender.method')
        Super.method(self)
        print('ending Extender.method')


class Provider(Super):  # Fill in a required method
    def action(self):
        print('in Provider.action')
    # pass

class Sub(Super):
    # pass
    def action(self):
        print('spam')

if __name__ == '__main__':
    # x = Inheritor()
    # x.method()dxsx
    for klass in (Inheritor, Replacer, Extender):
        print('\n' + klass.__name__ + '...')
        klass().method()
    print('\nProvider...')
    x = Provider()
    x.delegate()
    x = Sub()
    x.delegate()
