input_file = open("input.txt", "r")
entriesArray = input_file.read().split("\n")
depth_measure_increase = 0

for i in range(3, len(entriesArray), 1):
    first_window = int(entriesArray[i-1]) + int(entriesArray[i-2]) + int(entriesArray[i-3])
    second_window = int(entriesArray[i]) + int(entriesArray[i-1]) + int(entriesArray[i-2])
    if second_window > first_window:
        depth_measure_increase += 1

print(f'{depth_measure_increase=}')