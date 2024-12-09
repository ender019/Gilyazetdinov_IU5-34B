from tasks.database import Database
from tasks.task123 import task1, task2, task3


def main():
    """Основная функция"""
    data = Database()
    task1(data)
    task2(data)
    task3(data)


if __name__ == '__main__':
    main()
