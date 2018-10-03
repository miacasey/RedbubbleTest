# priceTest.py
# Import the totalPrice module to run the program and the unittest module to run test cases
from main import TotalPrice
import unittest

class testPriceCalculator(unittest.TestCase):
    def test1(self):
        # test cart-4560
        self.assertEqual(TotalPrice('test/test_carts/cart-4560.json', 'test/base_prices.json').returnPrice(), '4560\n')
    def test2(self):
        # test cart-9363
        self.assertEqual(TotalPrice('test/test_carts/cart-9363.json', 'test/base_prices.json').returnPrice(), '9363\n')
    def test3(self):
        # test cart-9500
        self.assertEqual(TotalPrice('test/test_carts/cart-9363.json', 'test/base_prices.json').returnPrice(), '9363\n')
    def test4(self):
        # test cart-11356
        self.assertEqual(TotalPrice('test/test_carts/cart-9500.json', 'test/base_prices.json').returnPrice(), '9500\n')
    def test5(self):
        # test custom-cart-8760
        self.assertEqual(TotalPrice('test/test_carts/custom-cart-8760.json', 'test/base_prices.json').returnPrice(), '8760\n')

if __name__ == '__main__':
    unittest.main()
