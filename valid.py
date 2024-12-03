def validate_name(name): 
    if not isinstance(name, str): 
        raise ValueError("The contact’s name must be a string.") 

def validate_phone_number(phone_number): 
    if not phone_number.isdigit(): 
        raise ValueError("The phone number must be an integer.")