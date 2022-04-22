class Rectangle: 
  def __init__(self, x, y, h, w):
    self.x = max(0, x)
    self.y = max(0, y)
    self.height = max(0, h)
    self.width = max(0, w)

  '''takes the parameters x, y, h, and w and assigns them to variables'''

  def __str__(self):
    string = "(x: {self.x}, y: {self.y}) width: {self.width}, height: {self.height}"
    return string

'''creates a string using variables from the init method and returns the string'''