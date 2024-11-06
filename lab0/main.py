from lab_python_fp.bisqur import *

if __name__ == '__main__':
    ur = BiSqUr(get_coef(1, "enter A"), get_coef(2, "enter B"), get_coef(3, "enter C"))
    print(*ur.get_solve())
