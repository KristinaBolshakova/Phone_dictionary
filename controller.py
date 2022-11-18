from os.path import exists
from reading_file import reading
from creating_file import creating


def file_none():
    path = 'Phone_dictionary.csv'
    valid = exists(path)
    if not valid:
        print(creating())
    reading()