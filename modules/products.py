import utils.validation as val

# Orchestrates the creation of a product by requesting and validating user input.
# Collects: ID (int), Name (string), and Price (float).
# Returns a tuple containing (product_id, product_name, unit_price).
def product_creation():
    
    product_id = val.request_data("ingresa el id del del producto: ", val.validate_int)
    product_name = val.request_data("Ingresa el nombre del producto: ", val.validate_string)
    unit_price = val.request_data("Ingresa el precio unitario dle producto: ", val.validate_float)
    
    return (product_id, product_name, unit_price)
