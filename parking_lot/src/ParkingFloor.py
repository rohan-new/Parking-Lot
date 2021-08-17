class ParkingFloor:
    def __init__(self, size):
        """
        Constructor for Parking Lot

        ARGS:
            size(int) - size of the parking lot
        """
        self.parkedCars = 0
        self.slots = dict.fromkeys([i for i in range(1, int(size)+1)])

    def increment_parked_cars(self):
        """
        will increment the number of parked cars
        """
        self.parkedCars += 1

    def decrement_parked_cars(self):
        """
        will decrement the number of parked cars
        """
        self.parkedCars -= 1

    def get_parked_cars(self):
        """
        getter for the number of parked cars
        """
        return self.parkedCars
    
    def get_empty_slots(self):
        """
        getter for the number of parked cars
        """
        return ((len(self.slots.keys()) - self.parkedCars) / len(self.slots.keys() ))* 100


    def get_slots(self):
        """
        getter for the parking slots
        """
        return self.slots

    def set_slots(self, slot, value):
        """
        setter for parking slots

        ARGS:
            slot(int) - where to place the incoming value
            value(Nonetype or Car object) - for setting the value on the given slot
        """
        self.slots[slot] = value
    
    def parking_lot_is_full(self):
        """
        checks whether parking lot is full or not

        ARGS:
            parkingLot(ParkingLot Object)
        """
        return len(self.get_slots()) <= self.get_parked_cars()
    

    