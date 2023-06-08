def get_unit(question):
    # Dictionary is ordered by unit length and value shows multiple
    units = {
        "kg": 1000,
        "ml": 1,
        "l": 1000,
        "g": 1,
    }
    
    while True:
        try:
            user_input = input(question)
            for unit in units:
                length = len(unit)
                if (user_input[-length:]).lower() == unit.lower():
                    user_number = float(user_input[:-length])

                    return user_number * units[unit]
            raise ValueError("Input must be a valid measurement of weight")
        except ValueError as error:
            print(error)