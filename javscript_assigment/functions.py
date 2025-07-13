# calculateDiscount(price, discount): Calculates the final price
# after applying a discount percentage.
# § Input: price (number), discount (number)
# § Output: Final price (number).

def calculate_discount(price, discount):
    if price < 0 or discount < 0 or discount > 100:
        raise ValueError("Invalid input")
    return price - (price * discount / 100)

# filterProducts(products, query): Filters a list of products by
# name based on a search query.
# § Input: products (array of objects with name and
# price), query (string)
# § Output: Filtered array of products.

def filter_products(products, query):
    if not isinstance(products, list) or not isinstance(query, str):
        raise ValueError("Invalid input")
    
    return [
        product for product in products
        if isinstance(product, dict) and 'name' in product and
           isinstance(product['name'], str) and
           query.lower() in product['name'].lower()
    ]

# sortProducts(products, key): Sorts a list of products by a
# specified key (name or price).
# § Input: products (array of objects with name and
# price), key (string)
# § Output: Sorted array of products.

def sort_products(products, key):
    if not isinstance(products, list) or key not in ('name', 'price'):
        raise ValueError("Invalid input")
    
    return sorted(products, key=lambda p: p[key])

# validateEmail(email): Validates an email address format.
# § Input: email (string)
# § Output: Boolean (true if valid, false otherwise).

import re
def validate_email(email):
    if not isinstance(email, str):
        raise ValueError("Invalid input")
    
    email_regex = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
    return re.match(email_regex, email) is not None




