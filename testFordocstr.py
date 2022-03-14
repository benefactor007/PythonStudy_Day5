# coding=utf-8

import docstr

if __name__ == '__main__':
    print(docstr.__doc__)
    print(docstr.func.__doc__)
    print(docstr.spam.__doc__)
    print(docstr.spam.method.__doc__)

    x = docstr.spam()
    x.method()