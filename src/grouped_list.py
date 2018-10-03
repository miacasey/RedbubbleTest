# Import the itertools groupby function
from itertools import groupby

class BasePriceList:
    '''
    This class implements a method to return a baseprice list that is regrouped by product types.
    '''
    # Function __init__ initializes the price dictionary that contains base prices grouped by product type
    #       Parameters: The baseprice list data we want to group
    #       Returns: N/A
    def __init__(self, bps):
        self.prices= {}
        for productType, prices in groupby(bps, key=lambda product: product["product-type"]):
            self.prices[productType] = list(prices)
