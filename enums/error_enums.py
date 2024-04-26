from enum import Enum


class ErrorMessage(Enum):
    INCORRECT_QUANTITY_ITEMS_CART = 'Invalid quantity of goods in the shopping cart'
    ERROR_SORTING_ASC = 'Error sorting by ascending'
    ERROR_SORTING_DESC = 'Error sorting by ascending'
    ERROR_SHOW = lambda items: f'Error, items on the page: {items}'
    ERROR_CATEGORY = 'Error, wrong product category'
    ERROR_PRICE_ITEM = 'Incorrect item price'
    ERROR_GRID = 'Wrong product display grid'
    ERROR_STATUS_ORDER = "Order status has not changed"
    ERROR_DELETE_ORDER = 'Error of order deletion'
    ERROR_TOTAL_PRICE = 'Total price of the whole order is incorrect.'
    ERROR_POSITIONS = 'Incorrect number of positions'
    ERROR_TOTAL_ITEMS = 'Incorrect number of items'
    ERROR_PRICE_PER_PIECE = 'Price error for one piece'
    ERROR_PUSH_MESSAGE = 'Invalid push notification message'
    ERROR_URL = 'Invalid URL'
