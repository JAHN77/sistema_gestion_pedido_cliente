# Generic input handler: prompts user and validates input based on the provided function.
# Returns the casted value (int, float, or stripped string).
def request_data(message, validator_function):
    while True:
        value = input(message)
        
        if validator_function(value):
            if validator_function == validate_int:
                return int(value)
            
            if validator_function == validate_float:
                return float(value)
                
            return value.strip()
    

# Validates that the input is a positive integer (> 0).
# Displays a red error message if validation fails.
def validate_int(number):
    try:
        number = int(number)
        if number > 0:
            return True
        else:
            print("\033[31mValues must be greater than 0 \033[0m\n")
            return False
    except ValueError:
        print("\033[31m------ Incorrect value ------\033[0m\n")
        return False


# Validates that the input is a positive float (> 0).
# Displays a red error message if validation fails.
def validate_float(number):
    try:
        number = float(number)
        if number > 0:
            return True
        else:
            print("\033[31mValues must be greater than 0 \033[0m\n")
            return False
    except ValueError:
        print("\033[31m------ Incorrect value ------\033[0m\n")
        return False


# Validates that the input is a non-empty string after stripping whitespace.
def validate_string(text):
    try:
        text = str(text).strip()
        if text != "":
            return True
        else:
            print("\033[31mValues cannot be empty\033[0m\n")
            return False
    except ValueError:
        print("\033[31m------ Incorrect value ------\033[0m\n")
        return False
    
# Validates the email format by checking for '@' and a domain with a dot.
# Displays a red error message if the format is invalid.
def validate_email(email):
    email = str(email).strip()
    if "@" in email and "." in email.split("@")[-1]:
            return True
    else:
        print("\033[31m------ Incorrect Value (ej: usuario@mail.com) ------\033[0m\n")
        return False