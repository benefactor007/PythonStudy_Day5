# coding=utf-8
# File updatedb.py: update Person object on database

if __name__ == '__main__':

    import shelve
    db = shelve.open('persondb')            # Reopen shelve with same filename

    for key in sorted(db):                  # Iterate to display database objects.
        print(key, '\t=>', db[key])         # Prints with custom format

    dynasty = db['Tianyuan Xu']             # Index by key to fetch
    # print(dynasty.__dict__.keys())
    print(list(name for name in dir(dynasty) if not name.startswith('__')))
    dynasty.giveRaise(.10)                  # Update in memory using class's method
    db['Tianyuan Xu'] = dynasty             # Assign to key to update in shelve
    print(dynasty)
    db.close()                              # Close after making changes