import numpy as np

arr =          [[ [[111, 112, 113], [121, 122, 123]],      \
                  [[211, 212, 213], [221, 222, 223]]  ],   \
                                                           \
               [  [[131, 132, 133], [141, 142, 143]],      \
                  [[231, 232, 233], [241, 242, 243]]  ],   \
                                                           \
               [  [[311, 312, 313], [321, 322, 323]],      \
                  [[331, 332, 333], [341, 342, 343]]  ]]   \

for d1 in range(3):
  for d2 in range(2):
    for d3 in range(2):
      print(arr[d1][d2][d3])
      

lst=[]

for d1 in range(3):
  for d2 in range(2):
    for d3 in range(2):
      lst[d1][d2][d3]=d1*100 + d2*10 + d3
      
for d1 in range(3):
  for d2 in range(2):
    for d3 in range(2):
      print(lst[d1][d2][d3])
      
      
