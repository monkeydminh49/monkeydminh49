class letter(object):
  def __init__(self):
    self.string = ''

  def getString(self):
    self.string = str(input(f'Nhap mot chuoi: '))
  
  def printString(self):
    print('Ket qua: '+self.string.upper()) #Viet hoa chuoi

M = letter()
M.getString()
M.printString()