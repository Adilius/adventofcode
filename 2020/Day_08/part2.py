import copy

accumulator = 0
nextInstruction = 0
changeInstructionIndex = 0

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
        #print("acc", int(instruction["acc"]))
        accumulator += int(instruction["acc"])
        nextInstruction += 1
    elif "jmp" in instruction:
        #print("jmp", int(instruction["jmp"]))
        nextInstruction += int(instruction["jmp"])
    elif "nop" in instruction:
        #print("nop", int(instruction["nop"]))
        nextInstruction += 1        

#Execute the instructions
def program(instructionsList):
    previousInstructions = []
    while nextInstruction not in previousInstructions and nextInstruction <= len(instructionsList)-1:
        previousInstructions.append(nextInstruction)
        executeInstruction(instructionsList[nextInstruction])
    print("Accumulator:", accumulator)
    if nextInstruction == len(instructionsList):
        print("Program ran successfully!")
        clearGlobals()
        return True
    else:
        print("Program ran unsuccessfully!")
        clearGlobals()
        return False

#Changes instruction with index
def changeInstruction(instructionsList):
    global changeInstructionIndex
    index = changeInstructionIndex
    print("index", index)

    if "nop" in instructionsList[index]:
        value = instructionsList[index]["nop"]
        instructionsList[index].pop("nop")
        instructionsList[index]["jmp"] = value
    elif "jmp" in instructionsList[index]:
        value = instructionsList[index]["jmp"]
        instructionsList[index].pop("jmp")
        instructionsList[index]["nop"] = value
    changeInstructionIndex += 1


#Clears globals for next program use
def clearGlobals():
    global accumulator
    global nextInstruction
    accumulator = 0
    nextInstruction = 0

def main():
    instructionsList = importInput("input.txt")
    instructionsListTemp = []

    
    while True:
        instructionsListTemp = copy.deepcopy(instructionsList)
        changeInstruction(instructionsListTemp)
        #print(instructionsListTemp)
        if program(instructionsListTemp):
            break
    print("Done")

if __name__ == "__main__":
    main()