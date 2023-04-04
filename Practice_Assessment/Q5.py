class Car:
    __discount = 25
    def __init__(self, price):
        self.price = price

    def purchase(self):
        total = self.price - self.price * Car.__discount / 100
        return(total)

car1=Car(600000)
car1.purchase()
print(Car.__discount)