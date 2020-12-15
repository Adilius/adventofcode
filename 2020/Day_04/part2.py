input_file = open("input.txt","r")
data = [x.strip() for x in input_file.readlines()]

#Takes dictionary as input
def validatePassport(passport):
    #Validate mandatory fields
    fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    for f in fields:
        if (f not in passport):
            return False
    
    #Validate numericals
    if not (1920 <= int(passport['byr']) <= 2002):
        return False
    if not (2010 <= int(passport['iyr']) <= 2020):
        return False
    if not (2020 <= int(passport['eyr']) <= 2030):
        return False

    #Validate height
    if 'cm' in passport['hgt'] and not (150 <= int(passport['hgt'][:-2]) <= 193):
        return False
    elif 'in' in passport['hgt'] and not (59 <= int(passport['hgt'][:-2]) <= 76):
        return False
    if 'cm' not in passport['hgt'] and 'in' not in passport['hgt']:
        return False

    #Validate strings
    if passport['ecl'] not in ['amb', 'blu', 'brn','gry','grn','hzl','oth']:
        return False

    validCharacters = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    if passport['hcl'][:1] == "#":
        for letter in passport['hcl'][1:]:
            if (letter not in validCharacters):
                return False
    else:
        return False

    if len(passport['pid']) != 9 or not passport['pid'].isdigit():
        return False

    return True

#Create an array of passports stored in passportArray
passport = {}
passportArray = []
validPassports = 0
#print(data)
for line in data:
    if line != '':
        for field in line.split():
            field, val = field.split(':')
            passport[field] = val
    else:
        print ("passport", passport)
        if validatePassport(passport):
            validPassports += 1
        passport = {}

print("Number of valid passports:", validPassports)