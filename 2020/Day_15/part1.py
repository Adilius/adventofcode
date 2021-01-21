input_file = open("input.txt", "r")
numbers = list(map(int,input_file.read().split(',')))

while len(numbers) < 2020:
    number = numbers[-1] #Get latest number
    if numbers.count(number) == 1: 
        numbers.append(0)
    else:
        last_spoken = [i for i,x in enumerate(numbers) if x == number]
        numbers.append(last_spoken[-1]-last_spoken[-2])

print(numbers[-1])