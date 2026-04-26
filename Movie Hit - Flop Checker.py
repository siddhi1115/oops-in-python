class Movie:
  def __init__(self,title,box_office):
    self.title = title
    self.box_office = box_office

  def display(self):
    print("Title:", self.title)
    print("Box office:", self.box_office)
    if self.box_office > 100:
      print("Hit!!!")
    else:
      print("Flop!!!")

m1 = Movie("Dhurandar",970000)
m1.display()