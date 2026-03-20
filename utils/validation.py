# Manejador de entrada genérico: solicita datos al usuario y los valida según la función proporcionada.
# Retorna el valor convertido (int, float o string sin espacios).
def request_data(message, validator_function):
    while True:
        value = input(message)
        
        if validator_function(value):
            if validator_function == validate_int:
                return int(value)
            
            if validator_function == validate_float:
                return float(value)
                
            return value.strip()
    

# Valida que la entrada sea un número entero positivo (> 0).
# Muestra un mensaje de error en rojo si la validación falla.
def validate_int(number):
    try:
        number = int(number)
        if number > 0:
            return True
        else:
            print("\033[31mLos valores deben ser mayores a 0 \033[0m\n")
            return False
    except ValueError:
        print("\033[31m------ Valor incorrecto ------\033[0m\n")
        return False


# Valida que la entrada sea un número decimal positivo (> 0).
# Muestra un mensaje de error en rojo si la validación falla.
def validate_float(number):
    try:
        number = float(number)
        if number > 0:
            return True
        else:
            print("\033[31mLos valores deben ser mayores a 0 \033[0m\n")
            return False
    except ValueError:
        print("\033[31m------ Valor incorrecto ------\033[0m\n")
        return False


# Valida que la entrada sea una cadena de texto no vacía tras eliminar espacios.
def validate_string(text):
    try:
        text = str(text).strip()
        if text != "":
            return True
        else:
            print("\033[31mLos valores no pueden estar vacíos\033[0m\n")
            return False
    except ValueError:
        print("\033[31m------ Valor incorrecto ------\033[0m\n")
        return False
    
# Valida el formato del correo verificando que contenga '@' y un dominio con punto.
# Muestra un mensaje de error en rojo si el formato es inválido.
def validate_email(email):
    email = str(email).strip()
    if "@" in email and "." in email.split("@")[-1]:
            return True
    else:
        print("\033[31m------ Valor incorrecto (ej: usuario@mail.com) ------\033[0m\n")
        return False
