def create_order(orders, customers, products, order_id, customer_id, product_id, quantity):
    """
    Funcionalidad 3: Registra un nuevo pedido usando diccionarios y tuplas.
    Calcula automáticamente el total.
    """
    # Validar que el cliente y el producto existan en los diccionarios de los compañeros
    if customer_id not in customers:
        return False, "Error: Cliente no encontrado."
    
    if product_id not in products:
        return False, "Error: Producto no encontrado."

    # Obtener información del producto (asumiendo tupla: id, nombre, precio)
    product_info = products[product_id]
    unit_price = product_info[2]
    product_name = product_info[1]
    
    # Obtener nombre del cliente (asumiendo diccionario de clientes)
    customer_name = customers[customer_id]['nombre']

    # Cálculo automático del total (Requerimiento funcional)
    total_order = unit_price * quantity

    # Almacenar en el diccionario de pedidos usando una tupla
    orders[order_id] = (customer_name, product_name, quantity, total_order)
    
    return True, orders

def get_orders(orders):
    """
    Funcionalidad 4: Permite visualizar los pedidos registrados.
    Retorna el diccionario para ser procesado por la interfaz.
    """
    if not orders:
        return "No hay pedidos registrados."
    
    return orders