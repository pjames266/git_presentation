import matplotlib.pyplot as plt

class Truck:
    """Truck Class
    """
    def __init__(self, make, year):
        """truck constructor

        Args:
            make (string): make/model of truck
            year (int): year of truck release
        """
        self.make = make
        self.year = year

    def __print__(self):
        
        return "I am a truck"

    
def __main__():
    optimus_prime = Truck("Peterbilt 379", 1992)
    print(optimus_prime)