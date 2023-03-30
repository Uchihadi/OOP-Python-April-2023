class Customer:
    def __init__(self, name, age, phone_no):
        self.__name = name
        self.__age = age
        self.__phone_no = phone_no

    def view_details(self):
        pass

    def update_details(self):
        pass

class Address:
    def __init__(self, door_no, street, area, pincode):
        self.__door_no = door_no
        self.__street = street
        self.__area = area
        self.__pincode = pincode

    def update_address(self):
        pass