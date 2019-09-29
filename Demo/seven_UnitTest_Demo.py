import unittest
from six_unit_test import Example

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("This will run before all the methods")

    def setUp(self):
        print("This will run before every method")

    def test_add(self):
        result = Example.addition(self, 10, 20)
        self.assertEqual(result, 30)
        self.assertEqual(Example.addition(self, -1, 2), 1)
        self.assertEqual(Example.addition(self, -10, 20), 10)

    def test_sub(self):
         result = Example.subtraction(self, 20, 10)
         self.assertEqual(result, 10)
         self.assertEqual(Example.subtraction(self, 40, 20), 20)
         self.assertEqual(Example.subtraction(self, 2, 4), -2)

    def test_mult(self):
         result = Example.multiplication(self, 2, 3)
         self.assertEqual(result, 6)

    def tearDown(self):
        print("This will run after every method")

    @classmethod
    def tearDownClass(cls):
        print("This will run after all the methods")

if __name__ == '__main__':
    unittest.main()