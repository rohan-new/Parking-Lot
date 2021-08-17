from ParkingFloor import ParkingFloor
from Vehicle import Car
from Constants import *


class ParkingLot:
    def __init__(self,size = None):
        self.parkingLot = self.create_parking_lot(size)

    
    def create_parking_lot(self,size):
        """
        creates a parking lot

        ARGS:
            size(str) - size of the parking lot
        """
        parkingLot = ParkingFloor(int(size))
        print('Created a parking slot with ' + size + ' slots')
        return parkingLot 

    def processEntry(self, parkingLot, registrationNumber, colour) :
        """
        will park the car in the parking lot and prints the allocated slot in the parking lot

        ARGS:
            parkingLot(ParkingLot Object)
            registrationNumber(str) - given registration number for the car
            colour(str) - given colour for the car
        """
        returnString = ''
        if parkingLot:
            if not self.parkingLot.parking_lot_is_full(): #if parking lot is not full
                parkingSlot = self.parkingLot.get_slots() #get all the available slots of the floor
                for slot in parkingSlot.keys():
                    if parkingSlot[slot] is None:
                        car = Car(registrationNumber, colour)
                        self.parkingLot.set_slots(slot, car)
                        car.set_slot(slot)
                        self.parkingLot.increment_parked_cars()
                        returnString = 'Allocated slot number: ' + str(slot)
                        break
            else:
                returnString = PARKING_LOT_IS_FULL_MESSAGE
        else:
            returnString = PARKING_LOT_NOT_CREATED
        return returnString
        

    def process_exit(self,parkingLot, inputSlot):
        """
        will leave the parking lot from desired slot and prints the leaving slot

        ARGS:
            parkingLot(ParkingLot Object)
            inputSlot(str) - given slot number
        """
        returnString = ''
        if parkingLot:
            if not self.parkingLot.get_parked_cars():
                returnString = 'Sorry, parking lot is empty'
            elif int(inputSlot) >= 1 and int(inputSlot) <= len(self.parkingLot.get_slots()):
                parkingSlot = self.parkingLot.get_slots()
                value = parkingSlot.get(int(inputSlot), None)
                if value is not None:
                    self.parkingLot.set_slots(int(inputSlot), None)
                    self.parkingLot.decrement_parked_cars()
                    returnString = 'Slot number ' + inputSlot + ' is free'
                else:
                    returnString = 'No car at Slot number ' + inputSlot
            else:
                returnString = 'Cannot exit slot: ' + inputSlot + ' as no such exist!'
        else:
            returnString = PARKING_LOT_NOT_CREATED
        return returnString
        
    def slot_by_colour(self,parkingLot, inputColour):
        """
        prints the slot number of the cars for the given colour

        ARGS:
            parkingLot(ParkingLot Object)
            inputColour(str) - given colour
        """
        returnString = ''
        if parkingLot:
            if not self.parkingLot.get_parked_cars():
                returnString = 'Sorry, parking lot is empty'
            else:
                flag = False
                parkingSlot = self.parkingLot.get_slots()
                for parkedCar in parkingSlot.values():
                    if parkedCar is not None:
                        if parkedCar.get_colour() == inputColour:
                            flag = True
                            returnString += str(parkedCar.get_slot()) + ', '
                if not flag:
                    returnString = 'Not found'
        else:
            returnString = PARKING_LOT_NOT_CREATED
        return returnString


    def slot_by_car_number(self,parkingLot, number):
        """
        prints the slot number of the cars for the given number

        ARGS:
            parkingLot(ParkingLot Object)
            number(str) - given registration number
        """
        returnString = ''
        if parkingLot:
            if not self.parkingLot.get_parked_cars():
                returnString = 'Sorry, parking lot is empty'
            else:
                flag = False
                parkingSlot = self.parkingLot.get_slots()
                for parkedCar in parkingSlot.values():
                    if parkedCar is not None:
                        if parkedCar.get_registration_number() == number:
                            flag = True
                            returnString += str(parkedCar.get_slot()) + ', '
                            # assuming that for the cars, there is one and only one registration number exits
                            break
                if not flag:
                    returnString = 'Not found'
        else:
            returnString = PARKING_LOT_NOT_CREATED
        return returnString
    
    def car_by_colour(self,parkingLot, inputColour):
        """
        prints the registration number of the cars for the given colour

        ARGS:
            parkingLot(ParkingLot Object)
            inputColour(str) - given Colour
        """
        returnString = ''
        if parkingLot:
            if not self.parkingLot.get_parked_cars():
                returnString = 'Sorry, parking lot is empty'
            else:
                flag = False
                parkingSlot = self.parkingLot.get_slots()
                for parkedCar in parkingSlot.values():
                    if parkedCar is not None:
                        if parkedCar.get_colour() == inputColour:
                            flag = True
                            returnString += parkedCar.get_registration_number() + ', '
                if not flag:
                    returnString = 'Not found'
        else:
            returnString = PARKING_LOT_NOT_CREATED
        return returnString
    
    def lot_status(self,parkingLot):
        """
        return the status of Parking Lot

        ARGS:
            parkingLot(ParkingLot Object)
        """
        returnString = ''
        if parkingLot:
            print('Slot No.\tRegistration No\tColour')
            parkingSlot = self.parkingLot.get_slots()
            for parkedCar in parkingSlot.values():
                if parkedCar is not None:
                    returnString += str(parkedCar.get_slot()) + '\t' + \
                        parkedCar.get_registration_number() + '\t' + \
                        parkedCar.get_colour() + '\n'
        else:
            returnString = PARKING_LOT_NOT_CREATED
        return returnString


   

   