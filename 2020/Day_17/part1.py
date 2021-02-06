#Prints the starting grid
def print_grid(grid):
    for row in grid:
        print(row)

#Triple nested list comprehension with conditionals
#Returns a list of neighbors to a point
def get_neighbors(x, y, z):
    return [
        (j, i, k)
        for j in range(x-1, x+2)
        for i in range(y-1, y+2)
        for k in range(z-1, z+2)
        if j != x or i != y or k != z
    ]

def add_shell(space):
    #Zip pair togheter items from tuples
    # * Unpacks an object to directly access variables
    X, Y, Z = zip(*space.keys())
    x1, x2 = min(X), max(X)
    y1, y2 = min(Y), max(Y)
    z1, z2 = min(Z), max(Z)
    for j in range(x1 - 1, x2 + 2):
        for i in range(y1 - 1, y2 + 2):
            for k in range(z1 - 1, z2 + 2):
                coord = (j, i, k)
                if coord not in space:
                    space[coord] = "."

def next_state(space):
    new_space = dict()
    add_shell(space)
    for coord, value in space.items():
        active_neighbors = 0
        for n_coords in get_neighbors(*coord):
            if space.get(n_coords, ".") == "#":
                active_neighbors += 1

        #If rules true, turn cube active
        if (value == "#" and 2 <= active_neighbors <= 3
            or value == "." and active_neighbors == 3):
            new_value = "#"
        #If rules false, turn cube inactive
        else:
            new_value = "."
        new_space[coord] = new_value
    return new_space

INPUT_FILE = "input.txt"
grid = [list(line.strip()) for line in open(INPUT_FILE)]
print_grid(grid)

shift = (1 - len(grid)) // 2 #Floor division
#Nested dictionary comprehension
#Creates the 3d-space
space = {
    (j + shift, i + shift, 0) : grid[i][j]
    for i in range(len(grid))
    for j in range(len(grid[i]))
}
print("shift:", shift)
print(space)

for _ in range(6):
    space = next_state(space)

print(list(space.values()).count("#"))
