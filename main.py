import data.storage
import modules.customers

def main_menu():
    while True:
        print("\n--- SISTEMA DE GESTIÓN DE CLIENTES ---")
        print("1. Registrar o Actualizar Cliente")
        print("4. Salir")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            modules.customers.register_or_update()
        elif opcion == "4":
            return

if __name__ == "__main__":
    main_menu()