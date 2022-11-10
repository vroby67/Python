
import numpy as np

a = np.array([9,22,7,0])
a = np.array([9,33,7,0])

res=""

for b in a:
  if b == 22:
    res=" è "

if not res:
  res=" non è "

print ("Il 22" + res + "presente nell'array")
