class Vehicle:
    def __init__(self, vehicleType, vehicleNumber):
        self.vehicleNumber = vehicleNumber
        self.vehicleType = vehicleType

class ParkingSpot:
    def __init__(self, section, spotNumber, level, vehicle):
        self.section = section
        self.spotNumber = spotNumber
        self.level = level
        self.vehicle = vehicle
        
    def park(self, vehicle):
        self.vehicle = vehicle
        self.vehicleType = vehicle.vehicleType

    def remove(self):
        self.vehicle = None

class Level:
    def __init__(self, sections, levelNumber):
        self.levelNumber = levelNumber
        self.sections = sections
        self.spotsPerSection = 15
        self.availableSpots = list(range(1, self.spotsPerSection * self.sections + 1)) # contains the spot number of available spot
        self.parkingSpots = {} # {"MSDIH15": ParkingSpot, ...} Contains the ParkingSpot Object with vehicle name as the key
        if self.levelNumber == 1:
            self.availableType = ["Bus", "Truck"]
        else:
            self.availableType = ["MotorCycle", "Car"]

    def findAvailableSpot(self):
        if not len(self.availableSpots): # no spot available
            return None
        else:
            # Check if there is free space in the section
            self.availableSpots.sort()
            allocatedSpot = self.availableSpots[0]
            allocatedSection = allocatedSpot % self.spotsPerSection + 1
            return ParkingSpot(allocatedSection, allocatedSpot, self.levelNumber, None)

    def park(self, vehicle):
        freeParkingSpot = self.findAvailableSpot()
        if not freeParkingSpot: # current level has no vacancy
            return None
        else:
            spotNum = freeParkingSpot.spotNumber
            freeParkingSpot.park(vehicle)
            self.parkingSpots[vehicle.vehicleNumber] = freeParkingSpot
            '''if spotNum in self.availableSpots:'''
            self.availableSpots.remove(spotNum)
            return spotNum

    def exit(self, number):
        if number in self.parkingSpots.keys():
            exitParkingSpot = self.parkingSpots[number]
            exitNumber = exitParkingSpot.spotNumber
            self.availableSpots.append(exitNumber)
            self.availableSpots.sort()
            exitParkingSpot.remove()
            del self.parkingSpots[number]
            return exitNumber
        return None

class ParkingLot:
    def __init__(self, levels):
        self.levels = levels

    def park(self, vehicle):
        if vehicle.vehicleType not in ["Bus", "Car", "Truck", "MotorCycle"]:
            print("Sorry, your vehicle type is not applicable.")
            return None
        for level in self.levels:
            if vehicle.vehicleNumber in level.parkingSpots.keys():
                print("Vehicle Exist.")
                return None
            if vehicle.vehicleType not in level.availableType:
                continue
            if spot:= level.park(vehicle):
                print("Please proceed to Level", level.levelNumber, ", Spot", spot)
                return spot
        print("Sorry, the parking lot is full")
        return None

    def exit(self, number):
        for level in self.levels:
            if spot := level.exit(str(number)):
                print("Level", level.levelNumber, ", Spot", spot, "is now available")
                return spot
        print("This vehicle is not found in the system!")
        return None