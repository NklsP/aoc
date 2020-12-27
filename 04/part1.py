# get lines to array
file = open('04/input1.txt', 'r')
Lines = file.read().splitlines()


class Passport:
    def __init__(self, entry):
        self.valid = False
        colonSplit = entry.split(":")
        
        self.byr = 0
        self.iyr = 0
        self.eyr = 0
        self.hgt = 0
        self.hcl = ""
        self.ecl = ""
        self.pid = 0
        numberOfKeyValues = len(colonSplit) - 1
        
        if numberOfKeyValues == 8:
            self.valid = True

        # check if only cid missing
        if numberOfKeyValues == 7: 
            if "cid:" not in entry:
                self.valid = True

        if self.valid:    
            self.byr = entry.split("byr:")[1].split(" ")[0]
            self.iyr = entry.split("iyr:")[1].split(" ")[0]
            self.eyr = entry.split("eyr:")[1].split(" ")[0]
            self.hgt = entry.split("hgt:")[1].split(" ")[0]
            self.hcl = entry.split("hcl:")[1].split(" ")[0]
            self.ecl = entry.split("ecl:")[1].split(" ")[0]
            self.pid = entry.split("pid:")[1].split(" ")[0]

            if not (int(self.byr) >= 1920 and int(self.byr) <= 2002):
                self.valid = False

            if not (int(self.iyr) >= 2010 and int(self.iyr) <= 2020):
                self.valid = False
            
            if not (int(self.eyr) >= 2020 and int(self.eyr) <= 2030):
                self.valid = False

            if "cm" in self.hgt:
                if not (int(self.hgt.split("cm")[0]) >= 150 and int(self.hgt.split("cm")[0]) <= 193):
                    self.valid = False
            elif "in" in self.hgt:
                if not (int(self.hgt.split("in")[0]) >= 59 and int(self.hgt.split("in")[0]) <= 76):
                    self.valid = False
            else:
                self.valid = False
            
            if "#" in self.hcl[0]:
                if (len(self.hcl.split("#")[1]) == 6):
                    print(self.hcl.split("#")[1])
                    banned = "ghijklmnopqrstuvwxyz"
                    for c in self.hcl.split("#")[1]:
                        if c in banned:
                            self.valid = False
            else:
                self.valid = False

            if self.ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                self.valid = False

            if len(self.pid) != 9:
                self.valid = False
            
            


entry = ""
newLines = []
counter = 0

lastElemCoutner = 1

for line in Lines:
    if lastElemCoutner >= len(Lines):
        entry = entry + " " + line
        newLines.append(entry)
        print("---")
        continue

    if line != "":
        entry = entry + " " + line
    else:
        newLines.append(entry)
        entry = ""

    lastElemCoutner = lastElemCoutner + 1

# print(Lines)
# print(newLines)

for entry in newLines:
    passport = Passport(entry)

    if passport.valid:
        counter = counter + 1

print("The number of valid passports =", counter)


        
    
