# class Parent:
#     def __init__(self,num):
#       self.__num=num
#     def get_num(self):
#       return self.__num
# class Child(Parent):
#     def __init__(self,num,val):
#       super().__init__(num)
#       self.__val=val
#     def get_val(self):
#       return self.__val
# son=Child(100,200)
# print(son.get_num())
# print(son.get_val())

# class Parent:
#     def __init__(self):
#         self.num=100

# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.var=200
#     def show(self):
#         print(self.num)
#         print(self.var)

# son=Child()
# son.show()

# class Parent:
#     def __init__(self):
#         self.__num=100

#     def show(self):
#         print("Parent:",self.__num)

# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.__var=10

#     def show(self):
#         print("Child:",self.__var)

# dad=Parent()
# dad.show()
# son=Child()
# son.show()

class Customer:
    def __init__(self):
        self.__cust_id = None
        self.__cust_name = None

    def get_cust_id(self):
        print("Normal customer")

    def get_cust_name(self):
        return self.__cust_name

    def set_cust_id(self, value):
        self.__cust_id = value

    def set_cust_name(self, value):
        self.__cust_name = value

class PrivilegedCustomer(Customer):
    def __init__(self):
        super().__init__()
        self.__overdraft_limit = None

    def get_overdraft_limit(self):
        return self.__overdraft_limit

    def set_overdraft_limit(self, value):
        self.__overdraft_limit = value

    def get_cust_id(self):
        print("Privileged Customer")

class RegularCustomer(Customer):
    def __init__(self):
        super().__init__()
        self.__min_balance = None

    def get_min_balance(self):
        return self.__min_balance

    def set_min_balance(self, value):
        self.__min_balance = value

r=RegularCustomer()
p=PrivilegedCustomer()
r.get_cust_id()
p.get_cust_id()