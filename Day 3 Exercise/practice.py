# class Customer:
#     def __init__(self,name,mobile):
#         self.name=name
#         self.mobile=mobile
# class Mobile:
#     def __init__(self,brand):
#         self.brand=brand
#     def unlock(self,cover):
#         print(cover.color)
# class Cover:
#     def __init__(self):
#         self.__color="red"
# Customer("Cus1",Mobile("Apple")).mobile.unlock(Cover())

class Customer:
    def __init__(self,name,mobile):
        self.name=name
        self.mobile=mobile
class Mobile:
    def __init__(self,brand):
        self.brand=brand
    def unlock(self,cover):
        cover.color="yellow"
class Cover:
    def __init__(self):
        self.color="red"
Customer("Cus1",Mobile("Apple")).mobile.unlock(Cover())
print(Cover().color)

class Trade:
    def __init__(self):
        self.__trade_detail = None

    def get_trade_detail(self):
        return self.__trade_detail

    def set_trade_detail(self, value):
        self.__trade_detail = value

class TradeDetail:
    def __init__(self):
        self.__trade_id = None
        self.__order_id = None

    def get_trade_id(self):
        return self.__trade_id

    def get_order_id(self):
        return self.__order_id

    def set_trade_id(self, value):
        self.__trade_id = value

    def set_order_id(self, value):
        self.__order_id = value

t=Trade()
tr=TradeDetail()
t=tr.get_order_id()