class circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
    def calculate_area(self):
        print("Area of circle",self.pi*self.radius*self.radius)
class rectangle:
        def __init__(self,length,breadth):
            self.length=length
            self.breadth=breadth
        def calculate_area(self):
            print("Area of circle",self.length*self.breadth)
        
def area(shape):
    shape.calculate_area()
cir=circle(2)
rect=rectangle(2,4)
area(cir)
area(rect)
    
