input_file = open("input.txt", "r")
lines = input_file.read().split("\n")

time = lines[0]
busses = lines[1].split(",")    #Split busses into its own elements
busses = [b for b in busses if b != "x"]    #Remove x's


#print(lines)
print(time)
print(busses)

shortestBuss = 999999999
bussID = 0
for buss in busses:
    i = 0
    while int(buss)*i < int(time):
        i += 1
    print(buss, ":",i*int(buss))
    if shortestBuss > i*int(buss):
        shortestBuss = i*int(buss)
        bussID = buss
print("shortestBuss", shortestBuss)
print("time to wait:", int(shortestBuss)-int(time))
print("bussID", bussID)
print("answer:", (int(shortestBuss)-int(time))*int(bussID))
