# coding=utf-8

class rec:
    pass

def main():
    rec.name = 'JoJo'
    rec.age = 28
    print(rec.name)
    x = rec()
    y = rec()
    print(x.name, y.name)
    x.name = 'Dynasty'
    print(rec.name, x.name, y.name)
    print(list(rec.__dict__.keys()))
    print(list(name for name in rec.__dict__ if not name.startswith('__')))
    print(list(x.__dict__.keys()))
    print(list(y.__dict__.keys()))
    print(x.name, x.__dict__['name'])
    print(x.age)
    print(x.__dict__['age'])
    print(x.__class__)




if __name__ == '__main__':
    main()

