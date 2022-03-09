# coding=utf-8

# import chapter28_pyStudy_03072022                                   # Load class with import
# dynasty = chapter28_pyStudy_03072022.Person("Tianyuan Xu")          # Go through module name
#
# from chapter28_pyStudy_03072022 import Person                       # Load class with from
# dynasty = Person("Tianyuan Xu")                                     # Use name directly

# File makedb.py: store Person objects on a shelve database

# from chapter28_pyStudy_03072022 import Person, Manager
# jon = Person("Jiahao Wu")                                               # Re-create objects to be stored
# dynasty = Person("Tianyuan Xu", job = "dev", pay = 100000)
# xiuge = Manager("Xuping Lu", pay = 50000)

if __name__ == '__main__':
    # import shelve
    # db = shelve.open('persondb')                                            # Filename where objects are stored
    # for obj in (jon,dynasty,xiuge):                                         # Use object's name attr as key
    #     db[obj.name] = obj                                                  # Store object on shelve by key
    # db.close()                                                              # Close after making changes

    # import glob
    # print(glob.glob('person*'))
    # print(open('persondb.dir'.read()))
    # print(open('persondb.dat', 'rb').read())

    import shelve
    db = shelve.open('persondb')                        # Reopen the shelve
    print(len(db))                                      # There 'records' stored
    print(list(db.keys()))                              # Keys is the index
    jon = db['Jiahao Wu']                               # Fetch jon by key
    print(jon)                                          # Runs __repr__ from AttrDisplay
    print(jon.lastName)                                 # Runs lastName from Person
    for key in db:                                      # Iterate, fetch, print
        print(key, '=>', db[key])
    for key in sorted(db):                              # Iterate by sorted keys
        print(key, '=>', db[key])

