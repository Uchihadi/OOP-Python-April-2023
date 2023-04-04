class A:
	def __init__(self):
		self.__x=100
a=A()
a.__x=200
print(a.__x)

class Test:
    @staticmethod
    def sample(): print("Hello World")
class Test2(Test):
    @staticmethod
    def sample(): print("Infosys")
    
Test2.sample()

class Parent:
    def __init__(self,num):
        self.num=num
    
class Child(Parent):
    pass
parent=Parent(200)
child=Child(100)
print(child.num)

class Parent1:
    def __init__(self):
        self.num=100
class Parent2():
    def __init__(self):
        self.num=200
        
class Sample(Parent2,Parent1):
    pass
print(Sample().num)

class Parent1:
    def __init__(self):
        self.num=100
class Parent2():
    def mtd(self):
        print(self.num)
        
class Sample(Parent1,Parent2):
    pass
Sample().mtd()

class Parent:
    def mtd(self):
        print("Parent")
class Child(Parent):
    def mtd(self):
        print("Child")
def change(o=Child()):
    o.mtd()
change(Child())

class Test1(Exception):
    pass
class Test2:
    def sample(self):
        try:
            raise Test1
        except Test1:
            print(1)
        finally:
            print(2)
try:
    Test2().sample()
except Test1:
    print(3)
finally:
    print(4)
    
class Parent:
    def mtd(self):
        return 100
class Child(Parent):
    def mtd(self):
        pass
print(Child().mtd())

class Parent:
   num=100
   def mtd(self):
       self.num=200
       return self.num+10
print(Parent().mtd())

class Parent:
    def mtd(self):
        return 100
class Child(Parent):
    def mtd(self,num=200):
        return num
print(Child().mtd())

print((1,2) + (3,4))