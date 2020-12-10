input_file = open("input.txt", "r")
lines = input_file.read().splitlines()  #Read whole file, split by newlines
lines = [int(i) for i in lines]
lines.sort()
lines.append(lines[-1]+3)
lines.insert(0,0)

answer = 1
i = 0
while i in range(len(lines)-4):
    print(i, lines[i])
    if lines[i]+4 == lines[i+4]:
        print("Three group")
        i += 2
        answer *= 7
    elif lines[i]+3 == lines[i+3]:
        print("Two group")
        i += 1
        answer *= 4
    elif lines[i]+2 == lines[i+2]:
        print("One group")
        answer *= 2
    i += 1

print(lines)
print("Answer:", answer)