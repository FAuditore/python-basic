import unittest

from func import my_div, my_sum


class MyTest(unittest.TestCase):
    def setUp(self): print('before every test')

    def test_plus(self): self.assertEqual(my_sum(1, 2), 3)

    def test_div(self):
        with self.assertRaises(ZeroDivisionError):
            my_div(3, 0)


if __name__ == '__main__':
    res = unittest.main(verbosity=3, exit=False)
