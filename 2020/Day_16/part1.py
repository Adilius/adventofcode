input_file = open("input.txt","r")
input_lines = input_file.readlines()

#print(*input_lines)

rules = []
tickets = []

for line in input_lines:
    if line[0].isalpha() and 'or' in line:
        #print("Rule")
        firstLow = line.split(' ')[-3].split('-')[0]
        firstHigh = line.split(' ')[-3].split('-')[1]
        secondLow = line.split(' ')[-1].split('-')[0]
        secondHigh = line.split(' ')[-1].split('-')[1][:-1]
        rules.append([firstLow, firstHigh, secondLow, secondHigh])
    #elif line[0].isalpha():
        #print("Your/nearby ticket")
    elif line[0].isnumeric():
        tickets.append(line.strip().split(','))
        #print("Ticket")

#print(rules)
#print(tickets)
error_rate = 0


for ticket in tickets[1:]:  #loop through each ticket, also skip the first one
    for field in ticket:  #Loop through each field
        for rule in rules:  #Loop through each rule
            if (int(rule[0]) <= int(field) <= int(rule[1])) or (int(rule[2]) <= int(field) <= int(rule[3])):
                break
            if rule == rules[-1]:
                error_rate += int(field)

print("Error rate:", error_rate)