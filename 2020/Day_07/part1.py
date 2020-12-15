input_file = open("input.txt", "r")
lines = input_file.readlines()

#Class bag, contains zero or more smallerbag
class Bag:
    def __init__(self, Bag, Contains):
        self.colour = Bag[0] + Bag[1]
        self.contains = []
        for i in range(0,len(Contains),3):
            SmallerBag1 = SmallerBag(Contains[i], Contains[i+1] + Contains[i+2])
            self.contains.append(SmallerBag1)       

#Class smallerbag, contains bag colour and count
class SmallerBag:
    def __init__(self, Count, Colour):
        self.colour = Colour
        self.count = Count
    def __str__(self):
        return self.colour

#Get the rules
rules = []
for line in lines:
    words = line.split()
    if "bag" in words: words = [x for x in words if x != "bag"]
    if "bag," in words: words = [x for x in words if x != "bag,"]    
    if "bag." in words: words = [x for x in words if x != "bag."]
    if "bags" in words: words = [x for x in words if x != "bags"]
    if "bags," in words: words = [x for x in words if x != "bags,"]
    if "bags." in words: words = [x for x in words if x != "bags."]
    if "contain" in words: words = [x for x in words if x != "contain"]
    if "no" in words: words = [x for x in words if x != "no"]
    if "other" in words: words = [x for x in words if x != "other"]
    rules.append(words)

#Convert rules into bags
bags = []
for i in range(len(rules)):
    Bag1 = Bag(rules[i][:2],rules[i][2:])
    bags.append(Bag1)
    print(Bag1.colour)

#Returns smaller bags of bag
def checkBag(bags, bag, level=0):
    #print("Colour:",bag.colour, level)
    if bag.colour == "shinygold" and level > 0:
        return True
    else:
        for smallerbag in bag.contains:
            if checkBag(bags, getBag(bags, smallerbag.colour), level+1):
                return True
    
#Returns bag given colour
def getBag(bags, colour):
    for bag in bags:
        if bag.colour == colour:
            return bag

goldshinyCount = 0

#Check for golden bags
for bag in bags:
    print("Checking bag:", bag.colour)
    if checkBag(bags, bag):
        print("True")
        goldshinyCount += 1
    print("--------------------------")

print("goldshinyCount:", goldshinyCount)