import time
class Car:
    """
    Car class
    """

    def __init__(self, registrationNumber, colour):
        """
        Constructor for Car object

        ARGS:
            registrationNumber(str) - given registration number of the car
            colour(str) - given colour of the car
        """
        self.carRegistrationNumber = registrationNumber
        self.carColour = colour
        self.carSlot = None
        self.entry_time = time.time()


    def set_slot(self, slot):
        """
        Setter for slot

        ARGS:
            slot(int) - the allocated slot for the car
        """
        self.carSlot = slot

    def get_slot(self):
        """
        Getter for slot
        """
        return self.carSlot

    def get_colour(self):
        """
        Getter for colour
        """
        return self.carColour

    def get_registration_number(self):
        """
        Getter for Registration Number
        """
        return self.carRegistrationNumber
    
    def get_entry_time(self):
        return self.entry_time
    
    