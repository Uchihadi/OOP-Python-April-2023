class Customer:
    def __init__(self, name, age, phone_no, address):
        self.name = name
        self.age = age
        self.phone_no = phone_no
        self.address = address

    def view_details(self):
        print (self.name, self.age, self.phone_no)    
        print (self.address.__door_no, self.address.__street, self.address.__pincode)

class Address:
    def __init__(self, door_no, street, pincode):
        self.__door_no = door_no
        self.__street = street
        self.__pincode = pincode

    def update_address(self):
        pass

add1=Address(123, "5th Lane", 56001)
cus1=Customer("Jack", 24, 1234, add1)

cus1.view_details()