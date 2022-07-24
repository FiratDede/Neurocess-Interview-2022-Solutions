"""
  This class is for creating a product object.
  Each product has a name, price and image link
  attribute
"""
class Product:
  def __init__(self, name, price,imageLink):
    self.name = name
    self.price=price
    self.imageLink=imageLink