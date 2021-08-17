
import sys
from Constants import *
from ParkingLot import ParkingLot 
from ParkingSystem import ParkingSystem

def executeCommand(parkingSystem, command):
    if command[0] == CREATE_PARKING_LOT: 
        # parkingLot = ParkingLot(command[1])
        parkingLot = parkingSystem.create_parking_lot(command[1],parkingSystem )
    elif command[0] == PARK_CAR:    
        print(parkingSystem.park_car(command[1], command[2]))

    # elif command[0] == PARK_CAR:    
    #     print(parkingSystem.processEntry(command[1], command[2]))
    # elif command[0] == CAR_DEPARTURE:
    #     print(parkingSystem.process_exit(parkingLot, command[1]))
    elif command[0] == LOT_STATUS:
        print(parkingSystem.system_status(parkingSystem).rstrip('\n'))
    # elif command[0] == SEARCH_SLOT_BY_CAR_NUMBER:
    #     print(parkingLot.slot_by_car_number(parkingLot, command[1]).rstrip(', '))
    # elif command[0] == SEARCH_CAR_BY_COLOUR:
    #     print(parkingLot.car_by_colour(parkingLot, command[1]).rstrip(', '))
    # elif command[0] == SEARCH_SLOT_BY_COLOUR:
    #     print(parkingLot.slot_by_colour(parkingLot, command[1]).rstrip(', '))
    else:
        print(INVALID_COMMAND)
    return parkingSystem 


def commandMode(parkingSystem):
    try:
        command = input().split()
        while command[0] != EXIT:
            parkingSystem = executeCommand(parkingSystem, command)
            command = input().split()
    except Exception as e:
        print(e)


def fileReaderMode(parkingLot, fileName):
    try:
        with open(fileName) as file:
            commands = file.readlines()
            for command in commands:
                action = command.replace('\n', '').split()
                if checkParkingLotCreation(parkingLot, action):
                    parkingLot = executeCommand(parkingLot, action)
                else:
                    print (PARKING_LOT_NOT_CREATED)

    except Exception as e:
        print(e)

def checkParkingLotCreation(parkingLot,command):
    if parkingLot is None and command[0] != CREATE_PARKING_LOT:
        return False
    return True

def main():
    parkingLot = None
    parkingSystem = ParkingSystem()
    print('arg--',sys.argv)
    if len(sys.argv) > 1:
        fileReaderMode(parkingSystem, sys.argv[1])
    else:
        commandMode(parkingSystem)


if __name__ == '__main__':
    main()
