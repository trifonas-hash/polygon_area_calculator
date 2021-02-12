class Rectangle():
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width_new):
    self.width = width_new
  def set_height(self, height_new):
    self.height = height_new

  def get_area(self):
    return self.width * self.height
  
  def get_perimeter(self):
    return (self.width + self.height) * 2

  def get_diagonal(self):
    return ((self.width**2) + (self.height**2))**(0.5)

  def get_picture(self):
    if (self.width >= 50) or (self.height >= 50):
      return "Too big for picture."
    else:
      picture = ""
      final_width = ""
      for i in range(0, self.width):
        final_width += "*"
      for i in range(0, self.height):
        picture += final_width + "\n"
    return picture

  def get_amount_inside(self, new_shape):
    return self.get_area()//new_shape.get_area()

  def __str__(self):
    return f"{type(self).__name__}(width={self.width}, height={self.height})"

class Square(Rectangle):
  def __init__(self, side):
    super().__init__(width = side, height = side)
  def __str__(self):
    return f"{type(self).__name__}(side={self.width})"
  
  def set_side(self, side_new):
    super().set_width(side_new)
    super().set_height(side_new)

  def set_width(self, width_new):
    self.set_side(width_new)
  def set_height(self, height_new):
    self.set_side(height_new)
