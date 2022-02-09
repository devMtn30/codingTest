X = int(input())
line = 1

while X > line:
  X -= line
  line += 1
if line % 2 == 0:
  ja = X
  mo = line-X+1
else:
  mo = X
  ja = line-X+1

print($"{ja}/{mo}")

  