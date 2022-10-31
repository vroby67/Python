bricks = int(input("Mattoni disponibili: "))
rowLen = 1
rows = 0
while bricks >= rowLen:
  bricks -= rowLen
  rowLen += 1
  rows += 1

print ("File complete: ", rows)
print ("Mattoni avanzati: ", bricks)