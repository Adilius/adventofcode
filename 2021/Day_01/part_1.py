input_file = open("input.txt", "r")
entriesArray = input_file.read().split("\n")
depth_measure_increase = 0

for i in range(1, len(entriesArray), 1):
    if int(entriesArray[i]) > int(entriesArray[i-1]):
        depth_measure_increase += 1

print(f'{depth_measure_increase=}')
