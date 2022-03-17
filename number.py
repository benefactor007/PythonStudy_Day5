# coding=utf-8
# File number.py

class Number:
    def __init__(self, start):  # On Number(start)
        self.data = start

    def __sub__(self, other):  # On instance - other
        return Number(self.data - other)  # Result is a new instance

class Indexer():
    def __getitem__(self, index):
        return index ** 2


if __name__ == '__main__':
    X = Number(5)
    Y = X - 2
    print(Y.data)
    X = Indexer()
    print(X[2])                 # X[i] calls X.__getitem__(i)
    for i in range(5):
        print(X[i], end= ' ')   # Runs __getitem__(X,i) each item


#  python3.5 -m timeit -n 1000 -r -5 -s "L = list(range(100))" "x = L.__len__()"
#  python3.5 -m timeit -n 1000 -r -5 -s "L = list(range(100))" "x = len(L)"
