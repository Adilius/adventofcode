input_file = open("input.txt", "r")
entriesArray = input_file.read().split("\n")

horizontal_position = 0
aim = 0
depth = 0

for entry in entriesArray:
    direction, value = entry.split(' ')
    if direction == "forward":
        horizontal_position += int(value)
        depth += aim * int(value)
    elif direction == "down":
        aim += int(value)
    elif direction == "up":
        aim -= int(value)

print(f'{horizontal_position=}')
print(f'{depth=}')
answer = horizontal_position * depth
print(f'{answer=}')
