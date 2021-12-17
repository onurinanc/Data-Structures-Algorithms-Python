from abc import ABCMeta, abstractmethod
import math

class Point:
  
  def __init__(self, x, y):
    self._x = x
    self._y = y
    
  def __str__(self):
    return "(" + str(self._x) + "," + str(self._y) + ")" 

  def shift(self, x, y):
    return Point(self._x + x, self._y + y)
    
class Shape(metaclass=ABCMeta):
  
  def __init__(self, x, y):
    self.leftTop = Point(x,y)
    self.points = [Point(x,y)]
    
  @abstractmethod
  def calculatePoints():
    """ Defines the points and add thems to the list """
  
  @abstractmethod
  def calculateArea():
    """ Calculates the area of the shape """
    
  @abstractmethod
  def calculatePerimeter():
    """ Calculates the perimeter of the shape"""
  
  @abstractmethod
  def move():
    """ Moves the object from one location to another """
    
class Rectangle(Shape):
    
  def __init__(self, leftTop, height, width):
        
    self._height = height
    self._width = width
    
    super().__init__(leftTop._x, leftTop._y)
  
  def calculatePoints(self):
    rightTop = self.leftTop.shift(self._width, 0)
    rightBottom = self.leftTop.shift(self._width, self._height)
    leftBottom = self.leftTop.shift(0, self._height)
    self.points.append(rightTop)
    self.points.append(rightBottom)
    self.points.append(leftBottom)
      
  def move(self, x, y):
      super().__init__(x, y)
      self.calculatePoints()
  
  def calculateArea(self):
      return self._height * self._width

  def calculatePerimeter(self):
      return 2 * self._height + 2 * self._width
      

class Circle(Shape):
      
  def __init__(self, leftTop, radius):
        
    self._radius = radius
    
    super().__init__(leftTop._x, leftTop._y)
    
  def calculatePoints(self):
    rightBottom = self.leftTop.shift(2 * self._radius, 2 * self._radius)
    self.points.append(rightBottom)
      
  def move(self, x, y):
    super().__init__(x, y)
    self.calculatePoints()
  
  def calculateArea(self):
    return math.pi * self._radius * self._radius

  def calculatePerimeter(self):
    return 2 * math.pi * self._radius

def Scenario():
    
  while(True):
    choice = input("Type of Shape (q for exit): \n")
    
    if choice == 'q':
      return
    
    elif choice == 'r':
      x, y, h, w = [int(x) for x in input("Coordinate ( leftTop ), height and width :").split()]
      r = Rectangle(Point(x,y), h, w)
      r.calculatePoints()
      PrintRectangle(x, y, h, w, r)
        
      x, y = [int(x) for x in input("Move object to the new coordinate ( leftTop ):").split()]
      r.move(x, y)
      PrintRectangle(x, y, h, w, r)
        
    elif choice == 'c':
      x, y, radius = [int(x) for x in input("Coordinates ( leftTop ) and radius :").split()]
      c = Circle(Point(x,y), radius)
      c.calculatePoints()
      PrintCircle(x, y, radius, c)
        
      x, y = [int(x) for x in input("Move object to the new coordinate ( leftTop ):").split()]
      c.move(x, y)
      PrintCircle(x, y, radius, c)
        
def PrintRectangle(x, y, h, w, r):
  print("--Rectangle--")  
  print("Height: {}".format(r._height))
  print("Width : {}".format(r._width))
  print("Left Top Point : {}".format(r.leftTop))
  print("Area : {:.2f}".format(r.calculateArea()))
  print("Perimeter : {:.2f}".format(r.calculatePerimeter()))
  print("Points:  {} {} {} {} ".format(r.points[0], r.points[1], r.points[2], r.points[3]))
  
  
def PrintCircle(x, y, radius, c):
  print("--Circle--")  
  print("Radius: {}".format(c._radius))
  print("Left Top Point : {}".format(c.leftTop))
  print("Area : {:.2f}".format(c.calculateArea()))
  print("Perimeter : {:.2f}".format(c.calculatePerimeter()))
  print("Points:  {} {} ".format(c.points[0], c.points[1]))
  
    
if __name__ == "__main__":
  Scenario()