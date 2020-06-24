# Parking Lot

## Parking lot layout
1. The parking lot has 3 levels.

2. Each level has 2 sections, each section has 15 spots.

3. A single spot can accommodate a Motorcycle, Car or a Bus/Truck.  
  >a. The type of vehicle a spot can accommodate is predefined.  
  >b. Level 1 can accommodate only Trucks/Buses.  
  >c. Level 2 and 3 can accommodate only Cars and Motorcycles.  
  >d. A parking spot can only accommodate one type of vehicle.  
  
4. There is only one entry to the parking lot.  

## Assumption
1. The input are case-sensitive so please follow the input format  
2. Each vehicle has its unique vehicle number:  
   For example Car KK45 and Truck KK45 cannot co-exist  
   If same vehicle number being input, "Vehicle Exist" will shown to the screen  
3. In each floor, there are two sections but not shown on the screen according to the requirements.  
   They are included in the code.  
4. The spots are numbered as 1 to 30 on each floor with the incremental distance:  
   i.e., 1 is the nearest, 30 is the farthest  
   The vehicle prefers going 2-30 rather than 3-1  
   
## Language Version
Python 3.8.3 (with := operator)

## Input format
You can have two types of inputs:
1. Entry:
Input: ENTRY Car TS07EH3768
Output: Please proceed to Level 2, Spot 5

2. Exit
Input: EXIT TS07EH3768
Output: Level 2, Spot 5 is now available
