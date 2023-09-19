class Cylinder():

    def __init__(self,height=1,radius=1):
        self.height=height
        self.radius=radius
        
    def volume(self):
        pie = 3.14
        return self.height * pie * (self.radius)**2


    def surface_area(self):
        pie=3.14
        top = pie * (self.radius**2)
    
        return (2*top) + (2*pie*self.radius*self.height) 
    
c = Cylinder(2,3)
c.volume()
c.surface_area()


class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1=coor1
        self.coor2=coor2
    
    def distance(self):
        #tuple unpacking
        x1,y1 = self.coor1
        x2,y2=self.coor2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5
    
    def slope(self):
        x1,y1 = self.coor1
        x2,y2=self.coor2
        return (y2-y1) /(x2-x1)
    
coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
li.distance()
li.slope()