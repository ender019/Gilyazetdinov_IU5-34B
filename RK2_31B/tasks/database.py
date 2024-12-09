from .dataclasses import Base, Table, TableBase

class Database():
    base: list[Base] = [
        Base(1, "Учебное заведение"),
        Base(2, "Магазин"),
        Base(3, "Социальная сеть"),
        Base(4, "Проект управления")
    ]

    table: list[Table] = [
        Table(1, "Студенты", 1, 5),
        Table(2, "Курсы", 3, 4),
        Table(3, "Преподаватели", 2, 6),
        Table(4, "Товары", 2, 7),
        Table(5, "Заказы", 1, 5),
        Table(6, "Клиенты", 4, 3),
        Table(7, "Пользователи", 1, 8),
        Table(8, "Сообщения", 1, 4),
        Table(9, "Друзья", 3, 2),
        Table(10, "Проекты", 1, 6),
        Table(11, "Задачи", 2, 5),
        Table(12, "Сотрудники", 3, 4)
    ]

    table_base: list[TableBase] = [
        TableBase(1, 3),
        TableBase(1, 9),
        TableBase(1, 5),
        TableBase(1, 11),
        TableBase(1, 7),
        TableBase(2, 2),
        TableBase(2, 8),
        TableBase(2, 4),
        TableBase(2, 6),
        TableBase(2, 10),
        TableBase(2, 12),
        TableBase(3, 10),
        TableBase(3, 1),
        TableBase(3, 5),
        TableBase(3, 7),
        TableBase(3, 3),
        TableBase(4, 12),
        TableBase(4, 6),
        TableBase(4, 9),
        TableBase(4, 3)
    ]

    def __init__(self):
        # Соединение данных один-ко-многим
        self.one_to_many = [(t.name, t.kol, b.name)
                       for b in self.base
                       for t in self.table
                       if t.base_id == b.id]

        # Соединение данных многие-ко-многим
        self.many_to_many_temp = [(b.name, tb.table_id)
                             for b in self.base
                             for tb in self.table_base if tb.base_id == b.id]

        self.many_to_many = [(base_name, t.name, t.kol)
                        for base_name, table_id in self.many_to_many_temp
                        for t in self.table if t.id == table_id]