input_file = open("input.txt", "r")

passwordsArray = input_file.read().split("\n")
del passwordsArray[-1]  #Remove last element from list, which is just and empty line
validPasswords = 0


for i in range(len(passwordsArray)):
    passwordsArray[i] = passwordsArray[i].replace('-',' ')
    passwordsArray[i] = passwordsArray[i].replace(':','')
    passwordsArray[i] = passwordsArray[i].split(' ')
    lowerLimit = int(passwordsArray[i][0])
    upperLimit = int(passwordsArray[i][1])
    letter = passwordsArray[i][2]
    password = passwordsArray[i][3]
    count = password.count(letter)
    if count <= upperLimit and count >= lowerLimit:
        validPasswords += 1

print("Amount of valid passwords:",validPasswords)