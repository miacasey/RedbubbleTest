# main.py
'''
This program will take 2 inputs:
1. a JSON file representing a cart, and
2. a JSON file representing a list of base prices.
The program will output the total price of the cart, in cents followed by a newline character.
'''

# Import the sys module to access our command-line arguments
# Import the python src modules containing all the classes and methods we need to calculate the total of our cart
import sys
from src.data import Data
from src.grouped_list import BasePriceList
from src.calculator import Calculator

class TotalPrice(object):
    '''
    This class implements a method to return the total price (sum) of all of the objects in the cart.
    '''
    # Function __init__ initializes our total price class
    #       Parameters: The file representing a cart, the file representing a list of base prices
    #       Returns: Nothing
    def __init__(self, cartFile, basePriceFile):
        cartFile = Data(cartFile)
        self.cart= cartFile.get_data()
        bpFile = Data(basePriceFile)
        self.baseprices= bpFile.get_data()
    # Function returnPrice
    #       Parameters: None
    #       Returns: The total price of the cart, in cents followed by a newline character
    def returnPrice(self):
        bps= BasePriceList(self.baseprices).prices
        total= 0
        calculate= Calculator(bps)
        for product in self.cart:
            total += calculate.get_price(product)
        return '{total}\n'.format(total=total)

if __name__ == '__main__':
    total = TotalPrice(cartFile= sys.argv[1], basePriceFile= sys.argv[2])
    total.returnPrice()
