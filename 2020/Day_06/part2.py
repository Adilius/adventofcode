input_file = open("input.txt","r")
lines = input_file.readlines()

count = 0
group = dict()
groupSize = 0
answer = 0
for line in lines:
    if line == "\n":    #New group
        for each in group.values(): #Check if any answer reach group size
            if each == groupSize:
                answer += 1
        print(group)
        group.clear()
        groupSize = 0
    else:
        groupSize += 1
    for character in line:  #One person
        if character != "\n":   #We have answers
            if character in group: 
                group.update({character: group[character]+1})   #Existing answer in group
            else:
                group.update({character: 1})    #New answer in group
for each in group.values():
            if each == groupSize:
                answer += 1
print(answer)