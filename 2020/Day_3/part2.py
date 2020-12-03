input_file = open("input.txt", "r")
slopeArray = input_file.read().split("\n")
slopeArray = slopeArray[:-1] #remove last empty row

x = 0
slope1hitCounter = 0
slope2hitCounter = 0
slope3hitCounter = 0
slope4hitCounter = 0
slope5hitCounter = 0


for i in range(len(slopeArray)):
    if slopeArray[i][x] == "#":
        #print("Hit tree")
        slope1hitCounter += 1
    x += 1
    if x > 30:
        x -= 31
print("Trees hit:", slope1hitCounter)
x = 0

for i in range(len(slopeArray)):
    if slopeArray[i][x] == "#":
        #print("Hit tree")
        slope2hitCounter += 1
    x += 3
    if x > 30:
        x -= 31
print("Trees hit:", slope2hitCounter)
x = 0

for i in range(len(slopeArray)):
    if slopeArray[i][x] == "#":
        #print("Hit tree")
        slope3hitCounter += 1
    x += 5
    if x > 30:
        x -= 31
print("Trees hit:", slope3hitCounter)
x = 0

for i in range(len(slopeArray)):
    if slopeArray[i][x] == "#":
        #print("Hit tree")
        slope4hitCounter += 1
    x += 7
    if x > 30:
        x -= 31
print("Trees hit:", slope4hitCounter)
x = 0

for i in range(len(slopeArray)):
    if slopeArray[i][x] == "#":
        #print("Hit tree")
        slope5hitCounter += 1
    x += 1
    i += 1
    if x > 30:
        x -= 31
print("Trees hit:", slope5hitCounter)

print("Answer:", slope1hitCounter*slope2hitCounter*slope3hitCounter*slope4hitCounter*slope5hitCounter)