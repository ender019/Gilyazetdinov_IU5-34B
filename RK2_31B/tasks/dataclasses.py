class Table():
    def __init__(self, id, name, base_id, kol):
        self.id = id
        self.name = name
        self.base_id = base_id
        self.kol = kol

class Base():
    def __init__(self, id, name):
        self.id = id
        self.name = name

class TableBase():
    def __init__(self, base_id, table_id):
        self.base_id = base_id
        self.table_id = table_id
