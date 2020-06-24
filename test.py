import unittest
from parkinglot import ParkingLot, Level, Vehicle

class MyTestCase(unittest.TestCase):
    def test(self):
        levels = [Level(2, 1), Level(2, 2), Level(2, 3)]    
        parkingLot = ParkingLot(levels)

        # Fill first level but one
        for i in range(1, 30): # 1-29
            parkingLot.park(Vehicle("Bus", str(i)))
        self.assertEqual(30, parkingLot.park(Vehicle("Bus","30")))
        self.assertEqual(None, parkingLot.park(Vehicle("Truck","31")))
        self.assertEqual(5, parkingLot.exit("5"))
        self.assertEqual(5, parkingLot.park(Vehicle("Truck","31")))

        #Fill second level and third level but 2
        for i in range(101, 159): # 101-158
            parkingLot.park(Vehicle("Car", str(i)))
        self.assertEqual(29, parkingLot.park(Vehicle("MotorCycle","159")))
        self.assertEqual(None, parkingLot.park(Vehicle("Bike","159")))
        self.assertEqual(None, parkingLot.park(Vehicle("Truck","1")))
        self.assertEqual(30, parkingLot.park(Vehicle("Car","160")))
        self.assertEqual(25, parkingLot.exit("125"))
        self.assertEqual(25, parkingLot.park(Vehicle("Car","161")))

if __name__ == '__main__':
    unittest.main()