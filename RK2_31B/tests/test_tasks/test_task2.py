from tasks.task123 import task2
from tests.conftest import base

class TestTask2:
    def test_task2_work(self, base):
        out = task2(base)
        assert len(out) == 4
        assert out == [
            ['Магазин', 5],
            ['Учебное заведение', 4],
            ['Проект управления', 3],
            ['Социальная сеть', 2],
        ]