class tinh_binh_phuong(object):
  def __init__(self):
    self.s = ''
  
  def square(self):
    self.s = self.s**2
    print('Dap so: '+str(self.s))

S = tinh_binh_phuong()
S.s = float(input('Tinh binh phuong: '))
S.square()