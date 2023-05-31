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
        self.name = "Truck"

    def __init__(self, make, year, name):
        """truck constructor

        Args:
            make (string): make/model of truck
            year (int): year of truck release
            name (string): name of truck
        """
        self.make = make
        self.year = year
        self.name = name

    def __str__(self):
        """_summary_

        Returns:
            String: String to print when called in print
        """
        
        return "My name is " + self.name

    
if __name__ == '__main__':
    optimus_prime = Truck("Peterbilt 379", 1992, "Optimus Prime")
    print(optimus_prime)