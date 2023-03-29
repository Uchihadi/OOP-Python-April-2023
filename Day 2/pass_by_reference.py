class Mobile:
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

def change_price(mobile_obj):
    mobile_obj.price = 3000

mob1=Mobile(1000, "Apple")
change_price(mob1)
print (mob1.price)

class Mobile:
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

    def change_price(mobile_obj):
        print ("Id of object inside function", id(mobile_obj))
        mobile_obj.price = 3000

mob1=Mobile(1000, "Apple")
print ("Id of object in driver code", id(mob1))

mob1.change_price()
print ("Price of mob1 ", mob1.price)