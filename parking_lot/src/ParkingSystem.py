from ParkingLot import ParkingLot
from Constants import *

class ParkingSystem:
    def __init__(self):
        self.parking_lot_list = []
        self.dispatch_rule = EVEN_DISTRIBUTION


    def create_parking_lot(self, size, parkingSystem=None):
        parkingLot = ParkingLot(size)
        self.parking_lot_list.append(parkingLot)
        return parkingSystem 
    
    def assign_dispatch_method(self, dispatch_method):
        self.dispatch_rule = dispatch_method
    
    def find_parking_lot_min_occupancy(self):
        max_empty_slots_count = 0
        parking_lot = None
        for lots in self.parking_lot_list:
            empty_slots_count = lots.parkingLot.get_empty_slots()
            if empty_slots_count > max_empty_slots_count:
                parking_lot = lots
                max_empty_slots_count = empty_slots_count
        return parking_lot 
    
    def park_car(self, registrationNumber, colour):
        if self.dispatch_rule == EVEN_DISTRIBUTION:
            parking_lot = self.find_parking_lot_min_occupancy()
            parking_lot.processEntry(parking_lot, registrationNumber, colour)

        elif self.dispatch_rule == FILL_FIRST:
            for parking_lot in self.parking_lot_list:
                if  not parking_lot.parking_lot_is_full():
                    print(parking_lot.processEntry(parking_lot, registrationNumber, colour))
                    break
        else :
            print('Invalid Dispatcher Method')
    
    def system_status(self, parkingSystem):
        ret = ""
        for parking_lot in self.parking_lot_list:
            ret += parking_lot.lot_status()
        return ret


            



    


            


    
