
for n in range(2,4):
  print(*map(lambda  i : i ** n, range(2,11,2)))

#print(list(map(lambda n1, n2: n1**n2, range(2,11,2), range(2,4))))

result = map(lambda n1, n2: n1+n2, num1, num2)