class SpecifRange(Exception):
    """
    if your selected number is specific range outside,
    you can send this error.
    Atributes:
    * classies = class
    * found = number
    * range (type list) = your choose range
    """
    def __init__(self, found, range : list , classies):
        message = f"{found} is less than {range[0]} and more than {range[1]}.\n\t{classies} is cannot be range"
        super().__init__(message)


class NegativeValue(Exception):
    """
    if number is negative and class is cannot take
    negative value,you can send this error.
    
    Atributes:
    * classies = class
    * found = number
    """
    def __init__(self, found , classies):
        message = f"{found} is a negative number.\n\t{classies} is cannot be negative"
        super().__init__(message)

class MissingValue(Exception):
    def __init__(self, found , must , classies):
        message = f"{found} must take {must} values in list.\n\t{classies} is cannot be {found} value"
        super().__init__(message)