# Redbubble Coding Test
Create a price calculator command-line program.
___
## Layout
- The main file for this program is the python file `main.py`
- All modules containing supporting classes and mthods are found in the `src` folder
- All tests are found in the `test` folder, with supporting test cart JSON files in the subsequent `test_carts` folder
- A sample test file of baseprices called `base_prices.json` is also in the `test` folder
___
## Running
- Open command line or Terminal and navigate to the directory you would like to copy this repository to. Clone this repository using:

```
git clone https://github.com/miacasey/RedbubbleTest.git
```
- Run the program `totalPrice.py` followed by a cart file argument and the baseprice file argument:

```
python totalPrice.py cart.json base_prices.json
```
Where:
- `cart.json` is path or URL to a JSON file representing a cart that satisfy cart schema
(*such as `test_carts/cart-4560.json`, `test_carts/cart-9363.json`, `test_carts/cart-9500.json`, `test_carts/cart-11356.json`, `test_carts/custom-cart-8760.json`*)

- `base_prices.json` is any path or URL to a JSON file representing a list of baseprices that satisfy the baseprice schema (*such as `base_prices.json`*)
___
## Testing
Unit tests can be found in `test/priceTest.py` and can be run using:
```
python priceTest.py
```
