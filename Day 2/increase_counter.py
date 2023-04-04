class Mobile:
    counter = 1000
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand
        self.mobile_id = Mobile.counter #Creating a variable for a counter
        Mobile.counter += 1 #Refer statice variable always with the className

mob1=Mobile(20000, "Apple")
mob2=Mobile(30000, "Apple")
mob3=Mobile(5000, "Samsung")

print("mobile_id for mob1 is", mob1.mobile_id)
print("mobile_id for mob2 is", mob2.mobile_id)
print("mobile_id for mob3 is", mob3.mobile_id)

print("Current value of counter is", Mobile.counter)
