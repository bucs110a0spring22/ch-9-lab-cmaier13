class Rectangle: 
  def __init__(self, x, y, h, w):
    self.x = max(0, x)
    self.y = max(0, y)
    self.height = max(0, h)
    self.width = max(0, w)

  def __str__(self):
    string = "(x: {}, y: {}) width: {}, height: {}"
    return string.format(self.x, self.y, self.width, self.height)