import copy

input_file = open("input.txt", "r")
lines = input_file.read().splitlines()

width = len(lines[0])
height = len(lines)

#Creating the map
layout = [[0 for x in range(width)] for y in range(height)]
for y in range(len(lines)):
    for x in range(len(lines[y])):
        layout[y][x] = lines[y][x]

def printMap(mapLayout):
    for i in range(len(mapLayout)):
        print(mapLayout[i])

def changeSeat(mapLayout, y, x):
    currentState = mapLayout[y][x]
    if currentState == ".":
        return "."
    adjacentCounter = 0
    #Check west side
    if x > 0:
        #print("West side avaliable")
        if mapLayout[y][x-1] == "#":
            adjacentCounter += 1
    #Check north-west
    if x > 0 and y > 0:
        #print("North-west side avaliable")
        if mapLayout[y-1][x-1] == "#":
            adjacentCounter += 1
    #Check north side
    if y > 0:
        #print("North side avaliable")
        if mapLayout[y-1][x] == "#":
            adjacentCounter += 1
    #Check north-east
    if x < width-1 and y > 0:
        #print("North-east side avaliable")
        if mapLayout[y-1][x+1] == "#":
            adjacentCounter += 1
    #Check east side
    if x < width-1:
        #print("East side avaliable")
        if mapLayout[y][x+1] == "#":
            adjacentCounter += 1
    #Check south-east side
    if x < width-1 and y < height-1:
        #print("South-east side avaliable")
        if mapLayout[y+1][x+1] == "#":
            adjacentCounter += 1
    #Check south side
    if y < height-1:
        #print("South side avaliable")
        if mapLayout[y+1][x] == "#":
            adjacentCounter += 1
    #Check south-west
    if x > 0 and y < height-1:
        #print("South-west side avaliable")
        if mapLayout[y+1][x-1] == "#":
            adjacentCounter += 1

    if adjacentCounter == 0:
        return "#"
    if adjacentCounter >= 4:
        return "L"
    return currentState

def nextRound(mapLayout):
    nextLayout = copy.deepcopy(mapLayout)   #Copy list
    for y in range(len(mapLayout)):
        for x in range(len(mapLayout[y])):
            nextLayout[y][x] = changeSeat(mapLayout, y, x)
    return nextLayout

def roundHandler(mapLayout):
    nextLayout = copy.deepcopy(mapLayout)
    while True:
        nextLayout = nextRound(nextLayout)
        #printMap(nextLayout)
        #print("--------------")
        if nextLayout == mapLayout:
            break
        mapLayout = copy.deepcopy(nextLayout)
    return mapLayout

def countOccupied(mapLayout):
    count = 0
    for i in range(len(mapLayout)):
        for j in range(len(mapLayout[i])):
            if mapLayout[i][j] == "#":
                count += 1
    return count

#printMap(layout)
#print("-")
layout = roundHandler(layout)
print("Occupied count:",countOccupied(layout))