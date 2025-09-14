class element:
    """Class representing a chemical element."""
    def __init__(self,name : str, atomic_number : int, feature : dict = "normal", ion_number=0, neutron_number=0):
        self.name = name
        self.symbol = name[::2].capitalize()
        self.atomic_number = atomic_number
        self.proton = atomic_number
        self.neotron = neutron_number
        self.ion = ion_number
        self.period = atomic_number // 8 + 1
        self.group = atomic_number % 8 + 1
        self.akb = atomic_number + neutron_number
        self.feature = feature ## tempure , radioactive, metal or ametal...

    def __repr__(self):
        return f"Element(name={self.name}, symbol={self.symbol}, atomic_number={self.atomic_number}, atomic_weight={self.atomic_weight})"

    def __str__(self):
        return f"{self.symbol}()"