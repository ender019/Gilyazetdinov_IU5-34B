from operator import itemgetter
from .database import Database


def task1(data: "Database"):
    print('Задание B1')
    searched_char = 'З'
    res_11 = [el for el in data.one_to_many if el[0][0] == searched_char]
    print(*res_11, sep='\n')
    return res_11


def task2(data: "Database"):
    print('\nЗадание B2')
    res_12_unsorted = [[el.name, 1000000] for el in data.base]
    for t in res_12_unsorted:
        t[1] = min(map(lambda i: i[1], list(filter(lambda i: i[2] == t[0], data.one_to_many))))
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(*res_12, sep='\n')
    return res_12


def task3(data: "Database"):
    print('\nЗадание B3')
    res_13 = sorted(data.many_to_many, key=itemgetter(1), reverse=True)
    print(*res_13, sep='\n')
    return res_13