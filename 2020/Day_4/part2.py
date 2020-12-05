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
passportArray.append(passport)
print("length:", len(passportArray))
print(passportArray)

def validatePassport(passport):
    #Passport length check
    if len(passport) <= 6 or len(passport) >= 9:
        print("Length invalid")
        return False
    #If passport 1 short, and not missing cid, automatically invalid
    if len(passport) == 7:
        for each in passport:
            if each[:3] == "cid":
                print("Short & cid invalid")
                return False
    for each in passport:
        if each[:3] == "byr":
            if int(each[4:]) < 1920 or int(each[4:]) > 2002:
                print("Invalid byr")
                return False

        if each[:3] == "iyr":
            if int(each[4:]) < 2010 or int(each[4:]) > 2020:
                print("Invalid iyr")
                return False

        if each[:3] == "eyr":
            if int(each[4:]) < 2020 or int(each[4:]) > 2030:
                print("Invalid eyr")
                return False

        if each[:3] == "hgt":
            if each[-2:] == "in":
                if int(each[4:-2]) < 59 or int(each[4:-2]) > 76:
                    return False
            elif each[-2:] == "cm":
                if int(each[4:-2]) < 150 or int(each[4:-2]) > 193:
                    print("Invalid hgt cm")
                    return False

        if each[:3] == "hcl":
            if each[4] != "#":
                print("Invalid hcl #")
                return False
            elif each[5:].isalnum() == False and len(each[5:]) == 6:
                print("Invalid hcl alnum")
                return False

        if each[:3] == "ecl":
            if each[4:] not in ['amb','blu','brn','gry','grn','hzl','oth']:
                print("Invalid ecl")
                return False
        
        if each[:3] == "pid":
            if len(each[4:]) != 9:
                print("Invalid pid")
                return False
    return True

numberOfValidPassports = 0
for i in range(len(passportArray)):
    if validatePassport(passportArray[i]):
        numberOfValidPassports += 1

print("Number of valid passports:", numberOfValidPassports)