import datos.almacenamiento
import utilidades.validacion as val

def registrar_o_actualizar():

    # 1. Captura de datos
    id_cliente = val.solicitar_dato("ID del cliente (número): ", val.validar_int)
    nombre_cliente = val.solicitar_dato("Nombre del cliente: ", val.validar_string)
    email_cliente = val.solicitar_dato("Correo electrónico: ", val.validar_email)

    # 2. Estructura del nuevo registro
    nuevo_dato_cliente = {
        "nombre": nombre_cliente, 
        "email": email_cliente
    }

    # 3. Guardar en el diccionario de almacenamiento
    datos.almacenamiento.clientes.update({id_cliente: nuevo_dato_cliente})
    print(f"Cliente {id_cliente} registrado/actualizado con éxito.")
