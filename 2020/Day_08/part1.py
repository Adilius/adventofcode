accumulator = 0
nextInstruction = 0

def importInput(input):
    input_file = open(input, "r")
    lines = input_file.read().split('\n')
    instructionsList = []
    for line in lines:
        instruction = {}
        instruction[line[:3]] = line[4:]
        instructionsList.append(instruction)
    return instructionsList

#Input a single dictionary instruction = {key:value}
def executeInstruction(instruction):
    global accumulator
    global nextInstruction

    if "acc" in instruction:
        print("acc", int(instruction["acc"]))
        accumulator += int(instruction["acc"])
        nextInstruction += 1
    elif "jmp" in instruction:
        print("jmp", int(instruction["jmp"]))
        nextInstruction += int(instruction["jmp"])
    elif "nop" in instruction:
        print("nop", int(instruction["nop"]))
        nextInstruction += 1        

#Execute the instructions
def program(instructionsList):
    previousInstructions = []
    while nextInstruction not in previousInstructions:
        previousInstructions.append(nextInstruction)
        executeInstruction(instructionsList[nextInstruction])
    print("Accumulator:", accumulator)

def main():
    instructionsList = importInput("input.txt")
    print(instructionsList)
    #print("Sending:",instructionsList[0])
    #executeInstruction(instructionsList[0])
    program(instructionsList)


if __name__ == "__main__":
    main()