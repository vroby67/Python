#import numpy as np

'''x = np.array([0, 1, -1, 90])
z = np.array([1,2,3])'''
x = [0, 1, -1, 90]
z = []

#nota bene: y è una copia e non istanza dell'array
for y in x:
  z.append(-y)
  y = y * (-1)
  
print (x)
print (z)
