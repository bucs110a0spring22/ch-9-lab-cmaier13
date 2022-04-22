from Rectangle import Rectangle 

class Surface: 
  def __init__(self, filename, x, y, h, w):
    self.rect = Rectangle(x,y,h,w)
    self.image = filename  

'''takes the parameters filename, x, y, h, w and assigns filename to a variable and uses the remaining parameters to create a rectangle object'''
  
  def getRect(self):
    return self.rect 

'''uses the rectangle object from init and returns the rectangle object '''