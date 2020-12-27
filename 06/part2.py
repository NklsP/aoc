# get lines to array
file = open('06/input1.txt', 'r')
Lines = file.read().splitlines()

class Group:
    def __init__(self):
        self.members = [] # Array of members
    
    def addToGroup(self, member):
        self.members.append(member)

class Member:
    def __init__(self, answer=""):
        self.answer = answer
    
    def __str__(self):
        return self.answer
    
    def __len__(self):
        return len(self.answer)

groups = []
group = Group()
member = Member()

# add to classes
for line in Lines:
    if  Lines.index(line) >= len(Lines) - 1:
        member = Member(line)
        group.addToGroup(member)

        # Reset        
        groups.append(group)
        group = Group()
        member = Member()
        continue
    if line == "":
        # Reset
        groups.append(group)
        group = Group()
        member = Member()
        continue
    else:
        member = Member(line)
        group.addToGroup(member)

numberOfCombinedYeses = 0

for g in groups:
    g1 = Group() 
    g1.members = sorted(g.members, key=len)

    biggest = set(g1.members[len(g1.members) - 1].answer)
    newBiggest = biggest

    for m in range(len(g1.members) - 1):
        biggest = newBiggest
        for c in biggest:
            if c not in g1.members[m].answer:
                newBiggest = newBiggest - set(c)
    
    numberOfCombinedYeses = numberOfCombinedYeses + len(newBiggest)

print(numberOfCombinedYeses)