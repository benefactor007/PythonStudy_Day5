# coding=utf-8

def dict_resource():
    D1 = {}
    D2 = {'name': 'Jiahao', 'age': '28'}
    E1 = {'ceo': {'name': 'jiahao', 'age': '28'}}
    D3 = dict(name='jiahao', age='28')
    D4 = dict([('name', 'jiahao'), ('age', '28')])
    keylist = ['name', 'age']
    valslist = ['jiahao', '28']
    D5 = dict(zip(keylist, valslist))
    D6 = dict.fromkeys(['a', 'b'], '5')
    #
    print(D2['name'])
    print(E1['ceo']['name'])
    if 'age' in D3 or D2:
        print('True')
    else:
        print('False')
    print(D2.keys())

    for i in [D1, D2, E1, D3, D4, D5, D6]:
        print(i)

    # Show more operation in Dict.
    print(D2.values())
    print(D2.items())
    D7 = D2.copy()
    print(D7)
    D2.clear()
    print(D2)
    D2.update(D7)
    print(D2)
    print(D2.get('name', 'Failure'))
    print(D2.get('year', 'Failure'))
    print(D2.pop('name', 'Does not exist'))
    print(D2.pop('name', 'Does not exist'))
    print(D2.setdefault('age','27'))
    print(D2.pop('age', 'Does not exist'))
    print(D2.setdefault('age', '18'))
    print(D2)
    D2.popitem()
    print(D2)
    print(len(D3))
    print(len(D2))
    D2['age'] = '18'
    print(D2)
    D2['age'] = '28'
    print(D2)
    del D2['age']
    print(D2)
    print(list(D2.keys()))              # ONLY in Python3.X
    print(list(D3.keys()))
    print(D7.keys() & D3.keys())        # 公共键
#     Dictionary views (Python 3.X)
    D8 = {x: x*2 for x in range(10)}
    print(D8)

    for element in D8:                  # D8.keys()
        print('x = ' + str(element) + '\t' + 'x*2 = ' + str(D8[element]))


def dict_searchValsAsKey():
    table = {'Holy Grail':              '1975',
             'Life of Brian':           '1979',
             'The Meaning of Life':     '1983'}
    print(table['Holy Grail'])
    print(list(table.items()))
    print([title for (title, year) in table.items() if year == '1975'])
    print(table['Holy Grail'])
    print([key for (key, value) in table.items() if value == '1975'])
    print([key for key in table.keys() if table[key] == '1975'])


def dict_nest_sample():
    rec = {'name'   :  'Bob',
           'jobs'   :  ['developer', 'manager'],
           'web'    :   'www.bobs.org/?bob',
           'home'   :   {'state': 'overworked', 'zip': '12345'}}
    print(rec['name'])
    print(rec['jobs'])
    print(rec['jobs'][1])
    print(rec['home']['state'])
    print(rec['home']['zip'])

    db = []
    db.append(rec)                      # A list "database"
    db.append('2')
    print(db[0]['jobs'])
    print((db))
    print(db[1])

    db2 = {}                        # A dictionary "database"
    db2['bob'] = rec
    db2['sue'] = '3'
    print(db2['bob']['jobs'])
    print(db2)

def main():
    # dict_resource()
    # dict_searchValsAsKey()
    dict_nest_sample()

if __name__ == '__main__':
    main()
