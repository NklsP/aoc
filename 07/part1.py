# get lines to array
file = open('07/input1.txt', 'r')
Lines = file.read().splitlines()

Rules = []

class Rule():
    def __init__(self, rule=""):
        self.rule = rule
        self.bag = ""
        self.contents = []
        self.quantitys = []

        self.bag = Bag(rule.split(" bags contain ")[0])

        if "no other bags." not in rule:
            for content in rule.split(" bags contain ")[1].split(","):
                self.quantitys.append(content.lstrip().split(" ")[0])
                self.contents.append(content.lstrip().split(content.lstrip().split(" ")[0])[1].strip())
    
    def __str__(self):
        return self.bag.color
    def __len__(self):
        return len(self.bag.color)
            

class Bag():
    def __init__(self, color):
        self.color = color
    def __str__(self):
        return self.color

# rule = Rule("drab tomato bags contain no other bags.")

# print(rule.bag.color)

# for q in rule.quantitys:
#     print(q)

# for c in rule.contents:
#     print(c.color)

for line in Lines:
    Rules.append(Rule(line))

containingShinyGold = []

for r in Rules:
    for c in r.contents:
        if "shiny gold" in c:
            containingShinyGold.append(r)

prevContainingShinyGold = []

counter = 0
ableToAppend = True

while ableToAppend:
    ableToAppend = False
    prevContainingShinyGold = containingShinyGold
    for r in Rules:
        for c in r.contents:
            for color in prevContainingShinyGold:
                if color.bag.color in c:
                    if r not in containingShinyGold:
                        ableToAppend = True
                        containingShinyGold.append(r)
                        counter = counter + 1

containingShinyGold = sorted(containingShinyGold, key=len)
for r in containingShinyGold:
    print(r.bag)

print(counter)
print(len(containingShinyGold))