#Storing a number of objects inside a list or a dictionary
class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

mob1=Mobile("Apple", 1000)
mob2=Mobile("Samsung", 2000)
mob3=Mobile("Apple", 3000)
mob4=Mobile("Samsung", 4000)
mob5=Mobile("Apple", 5000)

list_of_mobiles=[mob1, mob2, mob3, mob4, mob5]

for mobile in list_of_mobiles:
    print (mobile.brand,mobile.price)

#Storing Objects in a Dictionary
class Mobile:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price

mob1=Mobile("Apple", 1000)
mob2=Mobile("Samsung", 5000)
mob3=Mobile("Apple", 3000)

mob_dict={
          "m1":mob1,
          "m2":mob2,
          "m3":mob3
          }

for key,value in mob_dict.items():
    if value.price > 3000:
        print (value.brand,value.price)

#List of Customer Objects **IMPORTANT**
class Customer:
    def __init__(self, cust_id, cust_name, location):
        self.cust_id = cust_id
        self.cust_name = cust_name
        self.location = location

list_of_customers = [Customer(101, 'Mark', 'US'),
Customer(102, 'Jane', 'Japan'),
Customer(103, 'Kumar', 'India')]

dict_of_customer = {}
for customer in list_of_customers:
    dict_of_customer[customer.location] = customer

print ("Customer name in India is "+dict_of_customer["India"].cust_name)

for key,value in dict_of_customer.items():
    print ("Location: "+key+", Name: "+value.cust_name+", Id: "+(str(value.cust_id)))
