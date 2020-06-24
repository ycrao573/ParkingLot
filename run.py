from parkinglot import ParkingLot, Level, Vehicle

levels = [Level(2, 1), Level(2, 2), Level(2, 3)]    
parkingLot = ParkingLot(levels)

print("\n====================================")
print("  Parking Lot Management System v0.0")
print("====================================\n\n")

while True:
    print("\nInput Intruction: (enter 'exit' to stop the system)")
    if line:=input():
        line = line.split()
        if line[0] == "exit":
            break
        if line[0] == "ENTRY" and len(line) == 3:
            parkingLot.park(Vehicle(line[1], line[2]))
        elif line[0] == "EXIT" and len(line) == 2:
            parkingLot.exit(line[1])
        else:
            print("Invalid Input!")