input_file = open("input.txt","r")
lines = input_file.readlines()

#Create an array of passports stored in passportArray
passport = []
passportArray = []
for line in lines:
    #Create new passport
    if line == '\n':
        passportArray.append(passport)
        passport = []
    #Append new information to current passport
    else:
        line = line[:-1]
        lineArray = line.split(' ')
        for each in lineArray:
            passport.append(each)

def validatePassport(passport):
    if len(passport) <= 6 or len(passport) >= 9:
        return False
    if len(passport) == 7:
        for each in passport:
            if each[:3] == "cid":
                return False
    return True

numberOfValidPassports = 0
for i in range(len(passportArray)):
    if validatePassport(passportArray[i]):
        numberOfValidPassports += 1

print("Number of valid passports:", numberOfValidPassports)