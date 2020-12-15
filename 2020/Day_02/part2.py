input_file = open("input.txt", "r")

passwordsArray = input_file.read().split("\n")
del passwordsArray[-1]  #Remove last element from list, which is just and empty line
validPasswords = 0


for i in range(len(passwordsArray)):
    passwordsArray[i] = passwordsArray[i].replace('-',' ')
    passwordsArray[i] = passwordsArray[i].replace(':','')
    passwordsArray[i] = passwordsArray[i].split(' ')
    firstCharacter = int(passwordsArray[i][0])
    secondCharacter = int(passwordsArray[i][1])
    letter = passwordsArray[i][2]
    password = passwordsArray[i][3]
    if (password[firstCharacter-1] == letter) != (password[secondCharacter-1] == letter):
        validPasswords += 1

print("Amount of valid passwords:",validPasswords)