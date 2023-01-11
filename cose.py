import unittest

value = True  # False


class Foo(unittest.TestCase):
    # Deve ritornare True o False
    def test(self):
        self.assertTrue(value)


unittest.main()