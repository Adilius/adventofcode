input_file = open("input.txt", "r")
slopeArray = input_file.read().split("\n")
slopeArray = slopeArray[:-1] #remove last empty row

TREE = "#"

#Different slopes
slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
slope_length = len(slopeArray)

#Multiplied tree count
multipliedTreeCounter = 1

for i in range(len(slopes)):
    slope_x = slopes[i][0]
    slope_y = slopes[i][1]
    #print("Slope_x:", slope_x)
    #print("Slope_y:", slope_y)
    x = y = 0   #Current pos
    treeCounter = 0
    while y < slope_length:
        #print(slopeArray[y])
        if slopeArray[y][x] == TREE:
            treeCounter += 1
        x += slope_x
        y += slope_y
        x = x % 31
    #print("Tree Counter:", treeCounter)
    multipliedTreeCounter *= treeCounter
print("Multiplied tree counter:", multipliedTreeCounter)