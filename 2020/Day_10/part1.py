input_file = open("input.txt", "r")
lines = input_file.read().splitlines()  #Read whole file, split by newlines
lines = [int(i) for i in lines]
lines.sort()
lines.append(lines[-1]+3)

oneDifference = 0
threeDifference = 0
previousJoltage = 0
for outlet in lines:
    if outlet - 3 == previousJoltage:
        threeDifference += 1
    else:
        oneDifference += 1
    previousJoltage = outlet

print(lines)
print("oneDifference:", oneDifference)
print("threeDifference:", threeDifference)
answer = oneDifference * threeDifference
print("Answer:", answer)