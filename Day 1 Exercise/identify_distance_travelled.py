#lex_auth_01275044879016755225
#Start writing your code here
class Vehicle:
    def __init__(self):
        self.mileage = None
        self.fuel_left = None
    
    def identify_distance_travelled(self, initial_fuel):
        # To find distance travelled is to use the fuel as a gauge
        distance_travelled = (initial_fuel - self.fuel_left) * self.mileage
        return distance_travelled
    
    def identify_distance_that_can_be_travelled(self):
        initial_fuel = 16
        distance_travelled = self.identify_distance_travelled(initial_fuel)
        
        if self.fuel_left > 5:
            return (initial_fuel - 5) * self.mileage - distance_travelled
        else:
            return 0
    
vehicle1 = Vehicle()
vehicle1.mileage = 10
vehicle1.fuel_left = 20
print (vehicle1. identify_distance_that_can_be_travelled())

