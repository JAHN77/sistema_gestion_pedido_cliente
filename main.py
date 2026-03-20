import modules.customers
import modules.products
import modules.orders

def main_menu():
    while True:
        # Display Menu Header
        print("\n--- CUSTOMER MANAGEMENT SYSTEM ---")
        print("1. Register or Update Customer")
        print("2. Register Product")
        print("3. Create Order")
        print("4. View Registered Orders")
        print("5. Exit")

        # Capture user selection
        choice = input("\nSelect an option: ")

        # Menu Logic using Structural Pattern Matching (Python 3.10+)
        match choice:
            case "1":
                # Redirects to the Customer Management module
                modules.customers.register_or_update()

            case "2":
                # Redirects to the Product Inventory module
                modules.products.register_product()

            case "3":
                # Redirects to the Order Creation module
                modules.orders.register_order()

            case "4":
                # Displays all orders stored in memory
                modules.orders.show_orders()

            case "5":
                # Clean exit from the loop
                print("Exiting system... Goodbye!")
                break

            case _:
                # Handle unexpected inputs
                print("Invalid option. Please try again.")


if __name__ == "__main__":
    # Ensure the script only runs if executed directly
    main_menu()