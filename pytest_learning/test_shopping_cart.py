from shopping_cart import ShoppingCart
from item_database import ItemDatabase
import pytest
from unittest.mock import Mock


@pytest.fixture
def cart():
    # all setup for the cart here...
    # It runs everytime I run function with cart as an argument
    # -> it doesn't reuse existing cart from other functions
    return ShoppingCart(5)


def test_can_add_item_to_cart(cart):
    cart.add('apple')
    assert cart.size() == 1


def test_when_item_added_then_cart_contains_item(cart):
    cart.add('apple')
    assert 'apple' in cart.get_items()


def test_when_add_more_than_max_items_should_fail(cart):
    for _ in range(5):
        cart.add('apple')
    with pytest.raises(OverflowError):
        cart.add('apple')


def test_can_get_total_price(cart):
    cart.add('apple')
    cart.add('orange')
    item_database = ItemDatabase()

    def mock_get_item(item):
        if item == 'apple':
            return 1.0
        if item == 'orange':
            return 2.0

    item_database.get = Mock(side_effect=mock_get_item)      # there is also return_value argument
    assert cart.get_total_price(item_database) == 3.0