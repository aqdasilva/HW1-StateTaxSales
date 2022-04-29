import main
import pytest


class items:
    def __init__(self, item_name, item_type, item_price):
        self.name = item_name
        self.type = item_type
        self.price = item_price


def test_cashout():
    shopping_cart = []
    shopping_cart.append(items('dior', "clothing", 2000))
    shopping_cart.append(items('avocdao', "wic", 2))
    shopping_cart.append(items('bmw', "other", 40000))


def test_more_cashout_MA():
    shopping_cart = []
    shopping_cart.append(items('dior', "clothing", 100))
    shopping_cart.append(items('avocdao', "wic", 200))
    shopping_cart.append(items('bmw', "other", 400))
    assert main.cashout_cart("MA", shopping_cart) == 700

def test_more_cashout_ME():
    shopping_cart = []
    shopping_cart.append(items('dior', "clothing", 100))
    shopping_cart.append(items('avocdao', "wic", 200))
    shopping_cart.append(items('bmw', "other", 400))
    assert main.cashout_cart("ME", shopping_cart) == 700

def test_more_cashout_NH():
    shopping_cart = []
    shopping_cart.append(items('dior', "clothing", 100))
    shopping_cart.append(items('avocdao', "wic", 200))
    shopping_cart.append(items('bmw', "other", 400))
    assert main.cashout_cart("NH", shopping_cart) == 700



# will fail because items are not on list or exist
def test_bad_items_MA():
    grocery_list = []
    grocery_list.append(items('Vacation', "luxury", 2000))
    grocery_list.append(items('portugal', "travel", 1500))
    grocery_list.append(items('bitcoin', "crypto", 40000))
    grocery_list.append(items('mana', "crypto", 34))
    assert main.cashout_cart("MA", grocery_list) == 43534

def test_bad_items_ME():
    grocery_list = []
    grocery_list.append(items('Vacation', "luxury", 2000))
    grocery_list.append(items('portugal', "travel", 1500))
    grocery_list.append(items('bitcoin', "crypto", 40000))
    grocery_list.append(items('mana', "crypto", 34))
    assert main.cashout_cart("ME", grocery_list) == 43534

def test_bad_items_NH():
    grocery_list = []
    grocery_list.append(items('Vacation', "luxury", 2000))
    grocery_list.append(items('portugal', "travel", 1500))
    grocery_list.append(items('bitcoin', "crypto", 40000))
    grocery_list.append(items('mana', "crypto", 34))
    assert main.cashout_cart("NH", grocery_list) == 43534


# fail because i just put strings everywhere
def test_strings():
    grocery_list = []
    grocery_list.append(items("testing testing", "should fail this string", "string"))
    grocery_list.append(items("tesing", "this", "string"))
    grocery_list.append(items("hopefully", "i got better", "at testing"))
    assert main.cashout_cart("ME", grocery_list) == "string because in class you said to test a string"


# test empty lists in every test
def test_empty_list():
    grocery_list = []
    grocery_list.append(items("", "", " "))
    grocery_list.append(items("", "", " "))
    grocery_list.append(items("", "", " "))
    assert main.cashout_cart("NH", grocery_list) == " "
    assert main.cashout_cart("MA", grocery_list) == " "
    assert main.cashout_cart("ME", grocery_list) == " "
