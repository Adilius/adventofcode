input_file = open("input.txt","r")
lines = input_file.readlines()

count = 0
answers = set()
for line in lines:
    if line == "\n":
        count += len(answers)
        print(answers)
        answers.clear()
    for character in line:
        #print(character)
        if character != "\n":
            answers.add(character)
count += len(answers)
print(answers)
answers.clear()
print(count)