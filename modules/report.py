

def get_total_orders(orders):
    return len(orders)

def calculate_daily_income(orders):
    return sum(order_info[3] for order_info in orders.values())

def get_orders_by_customer(orders):
    grouped = {}
    for order_id, order_data in orders.items():
        customer_name = order_data[0]  # primer elemento de la tupla
        if customer_name not in grouped:
            grouped[customer_name] = {}
        grouped[customer_name][order_id] = order_data
    return grouped

def get_sold_products(orders):
    sold = {}
    for order_id, order_data in orders.items():
        product_name = order_data[1]  # segundo elemento
        quantity = order_data[2]       # tercer elemento
        if product_name not in sold:
            sold[product_name] = 0
        sold[product_name] += quantity
    return sold

def generate_final_report(orders):
    report = {
        "total_orders": get_total_orders(orders),
        "total_income": calculate_daily_income(orders),  # ← agregar esto
        "orders_by_customer": get_orders_by_customer(orders),
        "sold_products": get_sold_products(orders),
    }
    return report

