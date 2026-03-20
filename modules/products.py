import utils.validation as val
from data.storage import products

# Orchestrator for product creation by requesting and validating user inputs.
# Captures: ID (integer), Name (string), and Price (float/decimal).
# Returns a tuple with (product_id, product_name, unit_price).
def product_creation():
    
    product_id = val.request_data("Enter product ID: ", val.validate_int)
    product_name = val.request_data("Enter product name: ", val.validate_string)
    unit_price = val.request_data("Enter product unit price: ", val.validate_float)
    
    return (product_id, product_name, unit_price)

def register_product():
    product = product_creation()
    
    # Check if the product ID (index 0 of the tuple) already exists in the storage
    if product[0] in products:
        print("This product already exists.")
    else:
        products[product[0]] = product
        print("Product registered successfully:", product)
