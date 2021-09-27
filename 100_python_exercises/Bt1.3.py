x = int(input('Nhap so nguyen: '))

d = dict()

for i in range (1, x+1):
  d[f'so chinh phuong cua {i}'] = i*i  #thêm giá trị vào dict
  
print(d)