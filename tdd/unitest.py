import unittest

class TestExample(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_adder(self):
        self.assertEqual(adder(1,2), 3)
        self.assertEqual(adder(2,2), 4)

def adder(a, b):
    if a == b == 2:
        return 5
    return a + b


if __name__ == '__main__':
    unittest.main()
