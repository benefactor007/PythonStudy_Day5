# coding=utf-8

import manynames

if __name__ == '__main__':
    # X = 66
    # print(X)                    # 66: the global here
    # print(manynames.X)          # 11: globals become attributes after imports
    #
    # manynames.f()               # 11: manynames's X, not the one here!
    # manynames.g()               # 22: local in other file's function
    #
    # print(manynames.C.X)        # 33: attribute of class in other module
    # I = manynames.C()
    # print(I.X)                  # 33: still from class here
    #
    # I.m()
    # print(I.X)                  # 55: now from instance!

    X = 11  # Global in module


    def g1():
        print(X)  # Reference global in module(11)


    def g2():
        global X
        X = 22  # Change global in module


    def h1():
        X = 33  # Local in function

        def nested():
            print(X)  # Reference local in enclosing(surround or close off on all sides.) scope(33)
        nested()


    def h2():
        X = 33  # Local in function

        def nested():
            nonlocal X  # Python 3.X statement
            X = 44  # Change local in enclosing scope

        nested()
        print(X)

    h1()
    h2()
