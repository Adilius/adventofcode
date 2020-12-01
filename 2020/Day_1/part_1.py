input_file = open("input.txt", "r")

entriesArray = input_file.read().split("\n")
iterationLength = len(entriesArray) - 1
#print(entriesArray)

entrySum = 0
goalSum = 2020
pointer1 = pointer2 = 0

def main():
    for pointer1 in range(iterationLength):
        for x in range(iterationLength - pointer1 - 1):
            pointer2 = x + pointer1 + 1
            entrySum = int(entriesArray[pointer1]) + int(entriesArray[pointer2])

            if entrySum == goalSum:
                print("Found match!", entriesArray[pointer1], "+", entriesArray[pointer2])
                print("Answer: ", int(entriesArray[pointer1]) * int(entriesArray[pointer2]))
                return 

if __name__ == "__main__":
    main()