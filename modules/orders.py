from data.storage import orders, customers, products
import utils.validation as val

def create_order(orders, customers, products, order_id, customer_id, product_id, quantity):

    # Verify if the customer exists in the database
    if customer_id not in customers:
        return False, "Error: Customer not found."

    # Verify if the product exists in the database
    if product_id not in products:
        return False, "Error: Product not found."

    # Extract product details (Tuple format: ID, Name, Price)
    product_info = products[product_id]
    unit_price = product_info[2]
    product_name = product_info[1]

    # Extract customer details
    customer_name = customers[customer_id]['name']

    # Calculate final transaction amount
    total_order = unit_price * quantity

    # Save the order as a tuple in the orders dictionary
    orders[order_id] = (customer_name, product_name, quantity, total_order)

    return True, orders

def get_orders(orders):

    if not orders:
        return "No registered orders found."

    return orders

def register_order():

    # Auto-generate Order ID based on current list size
    order_id = len(orders) + 1

    # Request validated data from the user
    customer_id = val.request_data("Customer ID: ", val.validate_int)
    product_id = val.request_data("Product ID: ", val.validate_int)
    quantity = val.request_data("Quantity: ", val.validate_int)

    # Attempt to process the business logic
    success, result = create_order(
        orders, customers, products,
        order_id, customer_id, product_id, quantity
    )

    # Print the resulting dictionary or the error message
    print(result)
    
def show_orders():

    result = get_orders(orders)
    print(result)