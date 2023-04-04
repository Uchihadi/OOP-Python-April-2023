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