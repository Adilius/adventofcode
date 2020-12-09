input_file = open("input.txt", "r")
lines = input_file.readlines()

full_list = []
for line in lines:
    full_list.append(int(line))

preamble = full_list[:25]
part_list = full_list[25:]
print("Preamble:",*preamble)
print("Part list:",*part_list)

def checkNum(preamble, target_num):
    for i, number in enumerate(preamble[:-1]):  #[:-1] because we do not need to check last number
        complementary = target_num - number
        if complementary in preamble[i+1:]:
            print("Solution: {} and {}".format(number, complementary))
            return number #Remove this from preamble
    else:
        print("No solution for:", target_num)
        return 0

def checkContiguous(cList, target_num):
    for x in range(len(cList)):
        contiguousSum = 0
        contiguousList = []
        cList2 = cList[x:]
        for y in range(len(cList2)):
            #print("Checking:", cList2)
            contiguousSum += cList2[y]
            contiguousList.append(cList2[y])
            #print("contiguousSum:", contiguousSum)
            if contiguousSum == target_num:
                print("Found contiguous")
                print(contiguousList)
                print(contiguousSum)
                contiguousList.sort()
                print("adding smallest and largest to get answer", sum(contiguousList[:1] + contiguousList[-1:]))
                return
            if contiguousSum > target_num:
                #print("contiguous over")
                break


for num in part_list:
    if checkNum(preamble, num) > 0:
        preamble.pop(0)
        preamble.append(num)
    else:
        break

checkContiguous(full_list, 22406676)
