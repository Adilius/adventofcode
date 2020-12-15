input_file = open("input.txt", "r")

entriesArray = input_file.read().split("\n")
iterationLength = len(entriesArray) - 1
#print(entriesArray)

entrySum = 0
goalSum = 2020
pointer1 = pointer2 = pointer3 = 0

def main():
    for x in range(iterationLength):
        pointer1 = x
        for y in range(iterationLength - pointer1 - 1):
            pointer2 = y + pointer1 + 1
            for z in range(iterationLength - pointer2 - 1):
                pointer3 = z + pointer2 + 1
                #print(pointer1, pointer2, pointer3)
                entrySum = int(entriesArray[pointer1]) + int(entriesArray[pointer2]) + int(entriesArray[pointer3])
                if entrySum == goalSum:
                    print("Found match!", entriesArray[pointer1], "+", entriesArray[pointer2] , "+", entriesArray[pointer3])
                    print("Answer: ", int(entriesArray[pointer1]) * int(entriesArray[pointer2]) * int(entriesArray[pointer3]))
                    return 


if __name__ == "__main__":
    main()