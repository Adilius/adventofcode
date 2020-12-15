input_file = open("input.txt", "r")
lines = input_file.readlines()

#Class bag, contains zero or more smallerbag
class Bag:
    def __init__(self, Bag, Contains):
        self.colour = Bag[0] + Bag[1]
        self.contains = []
        for i in range(0,len(Contains),3):
            SmallerBag1 = SmallerBag(int(Contains[i]), Contains[i+1] + Contains[i+2])
            self.contains.append(SmallerBag1)       

#Class smallerbag, contains bag colour and count
class SmallerBag:
    def __init__(self, Count, Colour):
        self.colour = Colour
        self.count = Count
    def __str__(self):
        return self.count + self.colour

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
    print(words)

#Convert rules into bags
bags = []
for i in range(len(rules)):
    print("---------------")
    currentBag = Bag(rules[i][:2],rules[i][2:])
    bags.append(currentBag)
    if len(currentBag.contains) > 0:
        print(currentBag.colour)
        for i in range(len(currentBag.contains)):
            print(currentBag.contains[i].count, currentBag.contains[i].colour)
    else:
        print(currentBag.colour)
    
#Returns bag given colour
def getBag(colour):
    for bag in bags:
        if bag.colour == colour:
            return bag

starterBag = getBag("shinygold")
answer = 0

def getInsideBag(bag):
    returnValue = 0
    #Check each inside bag
    for i in range(len(bag.contains)):
        count = bag.contains[i].count #Get the count
        insideValue = getInsideBag(getBag(bag.contains[i].colour)) #Go inside
        returnValue += (insideValue+1) * count
    return returnValue

print(getInsideBag(starterBag))
