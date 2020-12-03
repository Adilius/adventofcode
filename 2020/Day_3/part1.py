input_file = open("input.txt", "r")
slopeArray = input_file.read().split("\n")
slopeArray = slopeArray[:-1] #remove last empty row

x = 0
hitCounter = 0

for i in range(len(slopeArray)):
    if slopeArray[i][x] == "#":
        print("Hit tree")
        hitCounter += 1
    x += 3
    if x > 30:
        x -= 31
    print("X:",x)
    print(slopeArray[i], len(slopeArray[i]))
print("Trees hit:", hitCounter)