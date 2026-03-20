import data.storage
import utils.validation as val

def register_or_update():
    # 1. Captura de datos
    customer_id = val.request_data("ID del cliente (número): ", val.validate_int)
    if customer_id in data.storage.customers:
        print(f"el cliente con ID {customer_id} si existe")
        confirm = input("Quieres actulizar los datos del cliente? (s/n)")
        if confirm != 's':
            print ("Operacion cancelada")
            return False
    else:
        print(f"El cliente con ID {customer_id} no existe.")
        # --- NUEVA PREGUNTA AQUÍ ---
        confirm_new = input("¿Deseas registrarlo como un nuevo cliente? (s/n): ").lower()
        if confirm_new != 's':
            print("Operación cancelada.")
            return False

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
