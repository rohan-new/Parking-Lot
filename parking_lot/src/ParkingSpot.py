class ParkingSpot():
  def __init__(self, number):
    self.__number = number
    self.__free = True
    self.__vehicle = None 

  def is_free(self):
    return self.__free

  def assign_vehicle(self, vehicle):
    self.__vehicle = vehicle
    free = False

  def remove_vehicle(self):
    self.__vehicle = None
    free = True

