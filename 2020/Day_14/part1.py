input_file = open("input.txt", 'r')
lines = input_file.read().splitlines()

memory = {}
currentMask = ""
currentMem = ""
currentAddress = ""

#Takes in mask an decimal value, returns decimal value after run through mask
def run_mask(mask, value):
    value = "{0:b}".format(int(value)).zfill(36)
    newValue = ""
    for x in range(len(value)):
        if mask[x] == 'X':
            newValue += value[x]
        elif mask[x] == '0':
            newValue += '0'
        elif mask[x] == '1':
            newValue += '1'
    return int(newValue, 2)

for line in lines:
    if line[:4] == "mask":
        currentMask = line.split("=")[1][1:]
        print("mask", currentMask)
    else:
        currentAddress = line.split("[")[1].split("]")[0]
        currentMem = line.split("=")[1][1:]
        currentMem = run_mask(currentMask, currentMem)
        print(currentAddress , currentMem)
        memory.update({currentAddress: currentMem})

print(memory)

memSum = 0
for x in memory:
    memSum += memory[x]
print(memSum)