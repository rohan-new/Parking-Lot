import unittest
from ParkingLot import ParkingLot


class TestParkingLotUtilities(unittest.TestCase): 
    """
    will test the endpoints
    """

    def test_create_parking_lot(self): 
        testParkingLot = ParkingLot(str(6))
        self.assertEqual(len(testParkingLot.parkingLot.get_slots()), 6)

    def test_parking_lot_is_full(self):
        testParkingLot = ParkingLot(str(6))
        self.assertEqual(testParkingLot.parkingLot.parking_lot_is_full(), True)


    def test_park_car_lot_allocated(self):
        testParkingLot = ParkingLot(str(6))
        testString = testParkingLot.processEntry(testParkingLot, 'KA-01-AA-1112', 'White')
        self.assertEqual('Allocated slot number: 1', testString)

    def test_park_car_lot_full(self):
        testParkingLot = ParkingLot(str(1))
        testString = testParkingLot.processEntry(testParkingLot, 'KA-01-AA-1112', 'White')
        testString = testParkingLot.processEntry(testParkingLot, 'KA-01-AA-1113', 'White')
        self.assertEqual('Sorry, parking lot is full', testString)

    def test_car_departure_empty(self):
        testParkingLot = ParkingLot(str(6))
        testString = testParkingLot.process_exit(testParkingLot, '1')
        self.assertEqual('Sorry, parking lot is empty', testString)

    def test_car_departure_free(self):
        testParkingLot = ParkingLot(str(6))
        testString = testParkingLot.processEntry(testParkingLot, 'KA-01-AA-1114', 'White')
        testString = testParkingLot.process_exit(testParkingLot, '1')
        self.assertEqual('Slot number 1 is free', testString) 

    def test_car_departure_cannot_exit(self):
        testParkingLot = ParkingLot(str(6))
        testString = testParkingLot.processEntry(testParkingLot, 'KA-01-AA-1115', 'White')
        testString = testParkingLot.process_exit(testParkingLot, '7')
        self.assertEqual('Cannot exit slot: 7 as no such exist!', testString)

    def test_car_departure_slot_free(self):
        testParkingLot = ParkingLot(str(6))
        testParkString = testParkingLot.processEntry(testParkingLot, 'KA-01-AA-1115', 'White')
        testExitString = testParkingLot.process_exit(testParkingLot, '2')
        self.assertEqual('No car at Slot number 2', testExitString)

    

    def test_car_by_colour(self):
        testParkingLot = ParkingLot(str(6))
        testParkString = testParkingLot.processEntry(testParkingLot, 'KA-01-AA-1117', 'White')
        testString = testParkingLot.car_by_colour(testParkingLot, 'White')
        self.assertEqual(testString, 'KA-01-AA-1117, ')

   

    def test_slot_by_colour(self):
        testParkingLot = ParkingLot(str(6))
        testParkString = testParkingLot.processEntry(testParkingLot, 'KA-01-AA-1117', 'White')
        testString = testParkingLot.slot_by_colour(testParkingLot, 'White')
        self.assertEqual(testString, '1, ')



if __name__ == '__main__':
    unittest.main()
