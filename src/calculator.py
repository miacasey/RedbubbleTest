# calculator.py
class Calculator:
    '''
    This class implements a method to get the price of a given
    product in the cart, using the baseprice list attribute in the initializer.
    '''
    # Function __init__ initializes the calculator that we'll use to calculate individual product prices'
    #       Parameters: The (grouped) baseprice list we'll be using
    #       Returns: Nothing
    def __init__(self, bps):
        self.BPlist= bps
    # Function get_price
    #       Parameters: The product we want to find the price of
    #       Returns: The price of the product
    def get_price(self, product):
        basePrice= self.BPlist.get(product["product-type"])
        options = product["options"]
        for op in basePrice:
            ops = op["options"]
            keys = set(options) & set(ops)
            if all([options[key] in ops[key] for key in keys]):
                artistMarkup = product["artist-markup"]
                quantity = product["quantity"]
                price = op["base-price"]
                return int((price + round(price * artistMarkup/100)) * quantity)
        return 0
