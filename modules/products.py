import utils.validation as val

# Orquestador para la creación de un producto solicitando y validando las entradas del usuario.
# Captura: ID (entero), Nombre (cadena) y Precio (decimal).
# Retorna una tupla con (product_id, product_name, unit_price).
def product_creation():
    
    product_id = val.request_data("Ingresa el ID del producto: ", val.validate_int)
    product_name = val.request_data("Ingresa el nombre del producto: ", val.validate_string)
    unit_price = val.request_data("Ingresa el precio unitario del producto: ", val.validate_float)
    
    return (product_id, product_name, unit_price)
