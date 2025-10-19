#class
class Calculator:#可以用m=C...,m.balabala来调用（外部）
    name='good culculator'#class的固有属性self
    def initial(self,price,height,width,weight):#calss的给定属性(>固有属性)
        self.price=price
        self.h=height
        self.w=width
        self.we=weight
    
    def add(self,x,y):
        result=x+y
        print(result)
    def minus(self,x,y):
        result=x-y
        print(result)
    def mul(self,x,y):
        result=x*y
        print(result)
    def divide(self,x,y):
        result=x/y
        print(result)
    
        
m=Calculator()
m.add(1,1)

