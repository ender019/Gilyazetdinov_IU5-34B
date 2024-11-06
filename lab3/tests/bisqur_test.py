import unittest
from lab_python_fp.bisqur import BiSqUr


class BiSqUrTest_1(unittest.TestCase):
    def setUp(self):
        self.bisqur = BiSqUr(1, -5, 4)

    def test_get_disc(self):
        self.assertEqual(self.bisqur.get_disc(), 9)

    def test_get_base_solve(self):
        self.assertEqual(sorted(self.bisqur.get_base_solve()), [1, 4])

    def test_get_solve(self):
        self.assertEqual(sorted(self.bisqur.get_solve()), [-2.0, -1.0, 1.0, 2.0])

class BiSqUrTest_2(unittest.TestCase):
    def setUp(self):
        self.bisqur = BiSqUr(1, 5, 4)

    def test_get_disc(self):
        self.assertEqual(self.bisqur.get_disc(), 9)

    def test_get_base_solve(self):
        self.assertEqual(sorted(self.bisqur.get_base_solve()), [-4, -1])

    def test_get_solve(self):
        self.assertEqual(self.bisqur.get_solve(), "no solution")


if __name__ == '__main__':
    unittest.main()
