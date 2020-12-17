input_file = open("input.txt", "r")
lines = input_file.read().split("\n")

global currentDirection
global east
global west
global north
global south

currentDirection = "east"
east = 0
west = 0
north = 0
south = 0

# Print ship info
def printShip():
    global currentDirection
    global east
    global west
    global north
    global south

    print("East:", east, "West:", west, "North:", north, "South:", south,"Sum distance:",east+west+north+south,  "Current direction:", currentDirection)


# Turns ship left
def turnLeft():
    global currentDirection
    if currentDirection == "east":
        currentDirection = "north"
    elif currentDirection == "north":
        currentDirection = "west"
    elif currentDirection == "west":
        currentDirection = "south"
    elif currentDirection == "south":
        currentDirection = "east"


# Turns ship left
def turnRight():
    global currentDirection
    if currentDirection == "east":
        currentDirection = "south"
    elif currentDirection == "south":
        currentDirection = "west"
    elif currentDirection == "west":
        currentDirection = "north"
    elif currentDirection == "north":
        currentDirection = "east"


# Turns ship given rotation direction and degrees
def turnShip(action, value):

    # Turn degrees to quarter turns
    turns = int(value / 90)

    # If left turn
    if action == "L":
        for i in range(turns):  # pylint: disable=unused-variable
            turnLeft()

    # If right turn
    elif action == "R":
        for i in range(turns):  # pylint: disable=unused-variable
            turnRight()

    # Else failure
    else:
        print("turnShipFailure")


# Moves ship
def moveShip(action, value):
    global currentDirection
    global east
    global west
    global north
    global south

    if action == "N":
        north += value
    elif action == "E":
        east += value
    elif action == "S":
        south += value
    elif action == "W":
        west += value
    elif action == "F":
        if currentDirection == "north":
            north += value
        elif currentDirection == "east":
            east += value
        elif currentDirection == "south":
            south += value
        elif currentDirection == "west":
            west += value


# Executes instruction
def executeInstruction(instruction):

    # Get the action of instruction
    action = instruction[:1]

    # Get the value of the action
    value = int(instruction[1:])

    if action in ["N", "E", "S", "W", "F"]:
        moveShip(action, value)
    elif action in ["L", "R"]:
        turnShip(action, value)

#Convert to manhattan distance
def convertDistance():
    global east
    global west
    global north
    global south

    if east > west:
        east -= west
        west = 0
    else:
        west -= east
        east = 0

    if north > south:
        north -= south
        south = 0
    else:
        south -= north
        north = 0



def main():
    print(lines)
    for i in range(len(lines)):
        executeInstruction(lines[i])
    convertDistance()
    printShip()


if __name__ == "__main__":
    main()