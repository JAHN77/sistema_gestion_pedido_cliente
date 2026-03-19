import data.storage
import utils.validation as val

def register_or_update():

        # 1. Captura de datos
    id_customer = val.request_data("ID del cliente (número): ", val.validate_int)
    name_customer = val.request_data("Nombre del cliente: ", val.validate_string)
    email_customer = val.request_data("Correo electrónico: ", val.validate_email)

        # 2. Estructura del nuevo registro
    new_data_customer = {
        "name": name_customer, 
        "email": email_customer
        }

    # 3. Guardar en el diccionario de storage
    data.storage.customers.update({id_customer: new_data_customer})
    print(f"Cliente {id_customer} registrado/actualizado con éxito.")