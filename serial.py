"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """Create initial starting serial number"""
        self.start = self.count = start

    def __repr__(self):
        """Representation of the SerialGenerator class"""
        return f"SerialGenerator start = {self.start} count = {self.count}"
    
    def generate (self):
        """Generate new serial number that has increased by 1"""
        self.count += 1
        return self.count - 1
    
    def reset(self):
        """Reset serial number to starting number"""
        self.count = self.start
