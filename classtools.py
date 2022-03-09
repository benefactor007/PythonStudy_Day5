# coding=utf-8

# File classtools.py(new)
"""Assorted class utilities and tools"""


# {miscellaneous, ˌmisəˈlānēəs,
# (of items or people gathered or considered together) of various types or from different sources.}
# he picked up the miscellaneous papers


class AttrDisplay:
    """
    Provides an inheritable(inˈherədəb(ə)l) display overload method that shows instance with their class
    names and a name=value pair for each attribute stored on the instance itself (but not attrs inherited from its
    class). Can be mixed into any class, and will work on any instance
    """
    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key, getattr(self, key)))
        return ','.join(attrs)

    def __repr__(self):
        return '[%s: %s]' % (self.__class__.__name__, self.gatherAttrs())

if __name__ == '__main__':
    class TopTest(AttrDisplay):
        count = 0

        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count + 1
            TopTest.count += 2

        # def gatherAttrs(self):            # Replaces method in AttrDisplay
        #     return "spam"

    class SubTest(TopTest):
        pass

    X, Y = TopTest(), SubTest()  # Make two instances
    print(X)  # Show all instance attrs
    print(Y)  # Show lowest class name


    # class Manager(Person, AttrDisplay):  # Define a subclass of Person; Inherit Person attrs
    #     def __init__(self, name, pay):  # Redefine constructor
    #         Person.__init__(self, name, 'mgr', pay)  # Run original with 'mgr'
    #
    #     def giveRaise(self, percent, bonus=.10):  # Redefine to customize; redefine at this level
    #         # self.pay = int(self.pay * (1 + percent + bonus))          # Bad: cut and pastel
    #         Person.giveRaise(self, percent + bonus)  # Good: augment original; instance.method(args..)
    #         # Call Person's version
    #         # Python will convert to class.method(instance,args...)
    # dynasty = Manager("Tianyuan Xu", 666666)
    # # dynasty = AttrDisplay("Tianyuan Xu", 666666)
    # print(dynasty.gatherAttrs())
    # # >> job = mgr, name = TianyuanXu, pay = 666666

    # dynasty = Person("Tianyuan Xu", 666666)
    # print(list(dynasty.__dict__.keys()))            # Instance attrs only;  3.X keys is a view, not a list
    # print(dir(dynasty))                             # + inherited attrs in classes; 3.X includes class type methods
    # print(len(dir(dynasty)))
    # # >> 30
    # print(list(name for name in dir(dynasty) if not name.startswith('__')))
    # # >> ['giveRaise', 'job', 'lastName', 'name', 'pay']