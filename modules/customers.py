import data.storage
import utils.validation as val

def register_or_update():
    # 1. Captura de datos
    customer_id = val.request_data("ID del cliente (número): ", val.validate_int)
    customer_name = val.request_data("Nombre del cliente: ", val.validate_string)
    customer_email = val.request_data("Correo electrónico: ", val.validate_email)

    # 2. Estructura del nuevo registro
    new_customer_data = {
        "name": customer_name, 
        "email": customer_email
    }

    # 3. Guardar en el diccionario de almacenamiento
    data.storage.customers.update({customer_id: new_customer_data})
    print(f"Cliente {customer_id} registrado/actualizado con éxito.")
