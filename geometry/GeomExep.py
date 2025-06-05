class SpecifRangeError(Exception):
    """
    if your selected number is specific range outside,
    you can send this error.
    Atributes:
    * classies = class
    * found = number
    * range (type list) = your choose range
    """
    def __init__(self, found, range : list , classies):
        super().__init__(f"{found} is less than {range[0]} and more than {range[1]}.\n\t{classies} is cannot be range")


class NegativeValueError(Exception):
    """
    if number is negative and class is cannot take
    negative value,you can send this error.
    
    Atributes:
    * classies = class
    * found = number
    """
    def __init__(self, found , classies):
        super().__init__(f"{found} is a negative number.\n\t{classies} is cannot be negative")

class MissingValueError(Exception):
    """"""
    def __init__(self, found , must , classies):
        super().__init__(f"{found} must take {must} values in list.\n\t{classies} is cannot be {found} value")

class NotSuitableObjectError(Exception):
    """"""
    def __init__(self, obj , classies):
        super().__init__(f"{obj} is not suitable to be a {classies} object")