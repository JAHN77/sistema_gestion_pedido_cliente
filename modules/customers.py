import data.storage
import utils.validation as val

def register_or_update():
    
    # 1. Data Capture & Verification
    # Initial check to see if we are dealing with a new or returning customer
    customer_id = val.request_data("Customer ID (number): ", val.validate_int)
    
    if customer_id in data.storage.customers:
        # Case: Customer exists, ask for update permission
        print(f"Customer with ID {customer_id} already exists.")
        confirm = input("Do you want to update the customer's data? (y/n): ").lower()
        if confirm != 'y':
            print("Operation canceled.")
            return False
    else:
        # Case: Customer is new, ask for registration permission
        print(f"Customer with ID {customer_id} does not exist.")
        confirm_new = input("Would you like to register them as a new customer? (y/n): ").lower()
        if confirm_new != 'y':
            print("Operation canceled.")
            return False

    #