import time
import json
import sys
from lab_python_fp.field import field
from lab_python_fp.gen_random import gen_random
from lab_python_fp.unique import Unique
from lab_python_fp.sort import compl
from lab_python_fp.print_result import *
from lab_python_fp.timer import *
from lab_python_fp.process_data import *

data = [4, -30, 100, -100, 123, 1, 0, -1, -4]

if __name__ == '__main__':
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'}
    ]

    print(field(goods, 'title'))
    print(field(goods, 'title', 'price'))

    print(*gen_random(5, 1, 3))

    # out = gen_random(50, 1, 30)
    # print(*out)
    # ls = Unique(out, ignore_case=1)
    # for el in ls: print(el, end=" ")
    # print("\n-")
    # for el in ls: print(el, end=" ")

    # result = sorted(data, key=compl)
    # print(result)
    # result_with_lambda = sorted(data, reverse=True)
    # print(result_with_lambda)

    # print('!!!!!!!!')
    # print(test_1())
    # test_1()
    # test_2()
    # test_3()
    # test_4()

    # with cm_timer_1():
    #     time.sleep(1.5)
    #
    # with cm_timer_2().maneger():
    #     time.sleep(2.5)

    # with open(path) as f:
    #     data = json.load(f)
    # with cm_timer_1():
    #     f4(f3(f2(f1(data))))