from tasks.task123 import task1
from tests.conftest import base

class TestTask1:
    def test_task1_work(self, base):
        out = task1(base)
        assert len(out) == 2
        assert out[0] == ('Заказы', 5, 'Учебное заведение')
        assert out[1] == ('Задачи', 5, 'Магазин')