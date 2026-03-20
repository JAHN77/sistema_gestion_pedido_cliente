import data.storage
import utils.validation as val

def register_or_update():
    # 1. Data Capture
    customer_id = val.request_data("Customer ID (number): ", val.validate_int)
    
    # Check if customer exists
    if customer_id in data.storage.customers:
        print(f"Customer with ID {customer_id} already exists.")
        confirm = input("Do you want to update the customer's data? (y/n): ").lower()
        if confirm != 'y':
            print("Operation canceled.")
            return False
    else:
        print(f"Customer with ID {customer_id} does not exist.")
        confirm_new = input("Would you like to register them as a new customer? (y/n): ").lower()
        if confirm_new != 'y':
            print("Operation canceled.")
            return False

    # 2. Collect customer data
    customer_name = val.request_data("Customer Name: ", val.validate_string)
    customer_email = val.request_data("Email Address: ", val.validate_email)

    # 3. Create customer record structure
    new_customer_data = {
        "name": customer_name,
        "email": customer_email
    }

    # 4. Save to storage dictionary
    data.storage.customers.update({customer_id: new_customer_data})

    # 5. Confirmation message
    print(f"Customer {customer_id} successfully registered/updated.")