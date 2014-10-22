# Basic class structure, documented for my understanding

class Enemy: # defines our class
  def __init__(self, x): # constructor function, that sets a private method x (int?)
    self.energy = x

  def get_energy(self): # method that invokes the class i.e. self
    print(self.energy) # print to screen the private method energy defined in the constructor

jason = Enemy(5)
sandy = Enemy(9)
string = Enemy('straw') # a string is ok for x and prints correctly

jason.get_energy()
sandy.get_energy()
string.get_energy()
#string.energy() # this fails as energy is not accessible outside the class