input_file = open("input.txt", "r")
lines = input_file.readlines()

full_list = []
for line in lines:
    full_list.append(int(line))

preamble = full_list[:25]
full_list = full_list[25:]
print("Preamble:",*preamble)
print("Full list:",*full_list)

def checkNum(preamble, target_num):
    for i, number in enumerate(preamble[:-1]):  #[:-1] because we do not need to check last number
        complementary = target_num - number
        if complementary in preamble[i+1:]:
            print("Solution: {} and {}".format(number, complementary))
            return number #Remove this from preamble
    else:
        print("No solution for:", target_num)
        return 0

for num in full_list:
    if checkNum(preamble, num) > 0:
        preamble.pop(0)
        preamble.append(num)
    else:
        break
